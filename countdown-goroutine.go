package main

import (
	"fmt"
	"sync"
	"time"
)

const Number uint = 1e9 // 1 Billion

func countdown(n uint, wg *sync.WaitGroup) {
	defer wg.Done()
	for n > 0 {
		n = n - 1
	}
	return

}

func main() {

	var wg sync.WaitGroup

	wg.Add(2)

	fmt.Printf("Counting down %d two goroutines\n", Number/2)

	start := time.Now()
	go countdown(Number/2, &wg)
	go countdown(Number/2, &wg)
	wg.Wait()
	end := time.Now()

	fmt.Printf("Took %v\n", end.Sub(start))

}
