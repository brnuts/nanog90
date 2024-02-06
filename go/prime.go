package main

import (
	"fmt"
	"math"
	"time"
)

func isPrime(n int) bool {
	if n <= 2 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func getPrimesInRange(start, end int) []int {
	var primes []int
	for num := start; num <= end; num++ {
		if isPrime(num) {
			primes = append(primes, num)
		}
	}
	return primes
}

func main() {
	start := 1
	end := int(1e7) // 10 millions

	fmt.Printf("Finding primes between %d and %d\n", start, end)
	startTime := time.Now()
	result := getPrimesInRange(start, end)
	endTime := time.Now()
	fmt.Println("Total prime numbers found:", len(result))
	fmt.Printf("Took %fs\n", endTime.Sub(startTime).Seconds())
}
