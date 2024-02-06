package main

import (
	"fmt"
	"sync"
	"time"
)

const NUMBER = 1_000_000_000

func flipSumRange(start, end int, wg *sync.WaitGroup, result chan<- int) {
	defer wg.Done()
	flipSum := 0
	for n := end; n >= start; n-- {
		if n%2 == 0 {
			flipSum += n
		} else {
			flipSum -= n
		}
	}
	result <- flipSum
}

func parallelFlipSum(numGoroutines int) int {
	result := make(chan int, numGoroutines)
	wg := sync.WaitGroup{}

	chunkSize := NUMBER / numGoroutines
	for i := 0; i < numGoroutines; i++ {
		start := 1 + i*chunkSize
		end := start + chunkSize - 1
		wg.Add(1)
		go flipSumRange(start, end, &wg, result)
	}

	go func() {
		wg.Wait()
		close(result)
	}()

	totalSum := 0
	for chunkSum := range result {
		totalSum += chunkSum
	}

	return totalSum
}

func main() {
	numGoroutines := 4

	fmt.Printf("Flipsum %d with %d goroutines\n", NUMBER, numGoroutines)
	startTime := time.Now()
	result := parallelFlipSum(numGoroutines)
	endTime := time.Now()

	fmt.Printf("Result = %d\n", result)
	fmt.Printf("Took %fs\n", endTime.Sub(startTime).Seconds())
}

