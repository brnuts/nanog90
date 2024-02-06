use std::time::Instant;

const NUMBER: i32 = 1_000_000_000;

fn flip_sum(start: i32, end: i32) -> i32 {
    let mut flip_sum = 0;
    for n in (start..=end).rev() {
        if n % 2 == 0 {
            flip_sum += n;
        } else {
            flip_sum -= n;
        }
    }
    flip_sum
}

fn main() {
    println!("Flipsum {}", NUMBER);
    let start_time = Instant::now();
    let result = flip_sum(1, NUMBER);
    let end_time = Instant::now();

    println!("Result = {}", result);
    println!("Took {}s", (end_time - start_time).as_secs_f64());
}

