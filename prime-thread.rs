use std::sync::{Arc, Mutex};
use std::thread;
use std::time::Instant;

fn is_prime(n: u64) -> bool {
    if n < 2 {
        return false;
    }
    let sqrt_n = (n as f64).sqrt() as u64;
    for i in 2..=sqrt_n {
        if n % i == 0 {
            return false;
        }
    }
    true
}

fn get_primes_within_range(start: u64, end: u64, result: Arc<Mutex<Vec<u64>>>) {
    let mut primes = Vec::new();
    for num in start..=end {
        if is_prime(num) {
            primes.push(num);
        }
    }
    result.lock().unwrap().extend(primes);
}

fn parallel_get_primes(start: u64, end: u64, num_threads: usize) -> Vec<u64> {
    let result = Arc::new(Mutex::new(Vec::new()));
    let mut handles = vec![];

    let chunk_size = (end - start + 1) / num_threads as u64;
    for i in 0..num_threads {
        let result_clone = Arc::clone(&result);
        let thread_start = start + i as u64 * chunk_size;
        let thread_end = start + (i + 1) as u64 * chunk_size - 1;

        handles.push(thread::spawn(move || {
            get_primes_within_range(thread_start, thread_end, result_clone);
        }));
    }

    for handle in handles {
        handle.join().unwrap();
    }

    Arc::try_unwrap(result).unwrap().into_inner().unwrap()
}

fn main() {
    let start = 1;
    let end = 10_000_000; // 10 Millions
    let num_threads = 4;

    println!("Finding primes between {} and {} using {} threads", start, end, num_threads);
    let start_time = Instant::now();
    let result = parallel_get_primes(start, end, num_threads);
    let end_time = Instant::now();

    println!("Total prime numbers found: {}", result.len());
    println!("Took {:.6}s", (end_time - start_time).as_secs_f64());
}

