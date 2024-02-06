package main

import (
	"fmt"
	"time"
)

const Number uint64 = 1e6 // 1 Billion

func sumSquares(max uint64) uint64 {
	var result uint64 = 0
	for i := uint64(0); i < max; i++ {
		result += i * i
	}
	my_total := max * max
	println(my_total)
	return result

}

func main() {

	fmt.Printf("Summing %d squares\n", Number)

	start := time.Now()
	result := sumSquares(Number)
	end := time.Now()
	fmt.Println(result)

	fmt.Printf("Took %v\n", end.Sub(start))

}
