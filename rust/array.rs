use std::time::Instant;

const ARRAY_SIZE: usize = 1_000_000_000; // Adjust the size based on your system's capabilities

fn calculate_sum(data: &[f64], start: usize, end: usize) -> f64 {
    let mut sum = 0.0;
    for i in start..end {
        sum += data[i];
    }
    sum
}

fn main() {
    let data = vec![0.5; ARRAY_SIZE];

    let start = Instant::now();
    let sum = calculate_sum(&data, 0, ARRAY_SIZE);
    let end = Instant::now();

    println!("Took {:?}", end.duration_since(start));

    if (sum - (ARRAY_SIZE as f64 / 2.0)).abs() > f64::EPSILON {
        println!("Failed sum: {}", sum);
    } else {
        println!("Total Sum: {}", sum);
    }
}
