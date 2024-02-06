package main

import (
	"fmt"
	"math"
	"sync"
	"time"
)

func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	//for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
	for i := 2; i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func getPrimesWithinRange(start, end int, wg *sync.WaitGroup, results chan<- []int) {
	defer wg.Done()

	var primes []int
	for num := start; num <= end; num++ {
		if isPrime(num) {
			primes = append(primes, num)
		}
	}

	results <- primes
}

func parallelGetPrimes(start, end, numGoroutines int) []int {
	var wg sync.WaitGroup
	results := make(chan []int, numGoroutines)

	chunkSize := (end - start + 1) / numGoroutines
	for i := 0; i < numGoroutines; i++ {
		wg.Add(1)
		fmt.Printf("starting one for range (%d, %d)\n", start+i*chunkSize, start+(i+1)*chunkSize-1)
		go getPrimesWithinRange(start+i*chunkSize, start+(i+1)*chunkSize-1, &wg, results)
	}

	go func() {
		wg.Wait()
		close(results)
	}()

	var allPrimes []int
	for primes := range results {
		allPrimes = append(allPrimes, primes...)
	}

	return allPrimes
}

func main() {
	start := 1
	end := int(math.Pow10(6)) // 1 Million
	numGoroutines := 4

	fmt.Printf("Finding primes between %d and %d using %d goroutines\n", start, end, numGoroutines)
	startTime := time.Now()
	result := parallelGetPrimes(start, end, numGoroutines)
	endTime := time.Now()

	fmt.Printf("Total prime numbers found: %d\n", len(result))
	fmt.Printf("Took %fs\n", endTime.Sub(startTime).Seconds())
}

