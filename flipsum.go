package main

import (
	"fmt"
	"time"
)

const NUMBER = 1_000_000_000

func flipSum(start, end int) int {
	var flipSum int
	for n := end; n >= start; n-- {
		if n%2 == 0 {
			flipSum += n
		} else {
			flipSum -= n
		}
	}
	return flipSum
}

func main() {
	fmt.Printf("Flipsum %d\n", NUMBER)
	startTime := time.Now()
	result := flipSum(1, NUMBER)
	endTime := time.Now()

	fmt.Printf("Result = %d\n", result)
	fmt.Printf("Took %fs\n", endTime.Sub(startTime).Seconds())
}

