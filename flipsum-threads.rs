use std::time::Instant;
use std::thread;

const NUMBER: i32 = 1_000_000_000;

fn flip_sum_range(start: i32, end: i32, result_sender: std::sync::mpsc::Sender<i32>) {
    let mut flip_sum = 0;
    for n in (start..=end).rev() {
        if n % 2 == 0 {
            flip_sum += n;
        } else {
            flip_sum -= n;
        }
    }
    result_sender.send(flip_sum).unwrap();
}

fn parallel_flip_sum(num_threads: usize) -> i32 {
    let chunk_size = NUMBER / num_threads as i32;
    let (result_sender, result_receiver) = std::sync::mpsc::channel();

    let mut handles = vec![];

    for i in 0..num_threads {
        let start = 1 + (i as i32) * chunk_size;
        let end = start + chunk_size - 1;
        let sender_clone = result_sender.clone();
        let handle = thread::spawn(move || flip_sum_range(start, end, sender_clone));
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    drop(result_sender); // Close the sender to signal that no more values will be sent

    let mut total_sum = 0;
    for chunk_sum in result_receiver {
        total_sum += chunk_sum;
    }

    total_sum
}

fn main() {
    let num_threads = 4;

    println!("Flipsum {} with {} threads", NUMBER, num_threads);
    let start_time = Instant::now();
    let result = parallel_flip_sum(num_threads);
    let end_time = Instant::now();

    println!("Result = {}", result);
    println!("Took {}s", (end_time - start_time).as_secs_f64());
}

