use std::time::{Instant};

static NUMBER: u64 = 1_000_000_000_000_000_000;

fn countdown(num: u64) {
    let mut i = num;
    while i > 0 {
        i -= 1;
    }
}

fn main() {
    println!("Counting down {:?}", NUMBER);
    let start_time = Instant::now();
    countdown(NUMBER);
    let elapsed_time = start_time.elapsed();
    println!("Took {:?}", elapsed_time);
}

