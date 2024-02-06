package main

import (
	"fmt"
	"time"
)

const Number uint = 1e9 // 1 Billion

func countdown(n uint) {
	for n > 0 {
		n = n - 1
	}
	return

}

func main() {

	fmt.Printf("Counting down %d\n", Number)

	start := time.Now()
	countdown(Number)
	end := time.Now()

	fmt.Printf("Took %v\n", end.Sub(start))

}
