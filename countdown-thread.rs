use std::time::{Instant};
use std::thread;

static NUMBER: u32 = 1_000_000_000;

fn countdown(num: u32) {
    let mut i = num;
    while i > 0 {
        i -= 1;
    }
}

fn main() {
    println!("Counting down two threads with {:?}", NUMBER/2);
    let start_time = Instant::now();
    let thread1 = thread::spawn(move || {
        countdown(NUMBER/2);
    });
    let thread2 = thread::spawn(move || {
        countdown(NUMBER/2);
    });
    thread1.join().unwrap();
    thread2.join().unwrap();
    let elapsed_time = start_time.elapsed();
    println!("Took {:?}", elapsed_time);
}

