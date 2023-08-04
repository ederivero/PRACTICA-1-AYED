package main

import (
	"fmt"
	"time"
)

func bubbleSort(arr []int) {
	n := len(arr)
	for i := 0; i < n-1; i++ {
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
}

func main() {
	arr := []int{1}
	inicio := time.Now()
	bubbleSort(arr)
	fin := time.Now()
	tiempoEjecucion := float64(fin.Sub(inicio).Seconds())
	fmt.Printf("Tiempo de ejecución: %.8f", tiempoEjecucion)
}
