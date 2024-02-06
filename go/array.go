package main

import "fmt"
import "time"

const arraySize = 1e8 // Adjust the size based on your system's capabilities

func calculateSum(data []float64, start, end int) float64 {
	var sum float64
	for i := start; i < end; i++ {
		sum += data[i]
	}
	return sum
}

func main() {
	data := make([]float64, arraySize)
	for i := 0; i < arraySize; i++ {
		data[i] = 0.5
	}

	start := time.Now()
	sum := calculateSum(data, 0, arraySize) 
	end := time.Now()
	fmt.Printf("Took %v\n", end.Sub(start))

	if sum != float64(arraySize/2) {
		fmt.Printf("Failed")
	} else {
		fmt.Printf("Total Sum: %f\n", sum)
	}
}
