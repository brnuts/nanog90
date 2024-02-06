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

fn get_primes_within_range(start: u64, end: u64) -> Vec<u64> {
    let mut primes = Vec::new();
    for num in start..=end {
        if is_prime(num) {
            primes.push(num);
        }
    }
    primes
}

fn main() {
    let start = 1;
    let end = 10_000_000; // 10 Millions
    println!("Finding primes between {} and {}", start, end);
    let start_time = Instant::now();
    let result = get_primes_within_range(start, end);
    let end_time = Instant::now();
    println!("Total prime numbers found: {}", result.len());
    println!("Took {:.6}s", (end_time - start_time).as_secs_f64());
}
