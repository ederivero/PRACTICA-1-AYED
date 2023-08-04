package main

import (
	"fmt"
	"math/rand"
	"time"
)

func selectionSort(arr []int) {
	n := len(arr)

	for i := 0; i < n-1; i++ {
		minIndex := i

		// Buscar el índice del elemento más pequeño en el subarreglo no ordenado
		for j := i + 1; j < n; j++ {
			if arr[j] < arr[minIndex] {
				minIndex = j
			}
		}

		// Intercambiar el elemento más pequeño con el primer elemento del subarreglo no ordenado
		if minIndex != i {
			arr[i], arr[minIndex] = arr[minIndex], arr[i]
		}
	}
}

func generateRandomArray(size, min, max int) []int {
	arr := make([]int, size)
	rand.Seed(time.Now().UnixNano())
	for i := 0; i < size; i++ {
		arr[i] = rand.Intn(max-min+1) + min
	}
	return arr
}

func main() {
	size := 50000 // Cantidad de números enteros en el arreglo
	min := 1      // Valor mínimo del número aleatorio generado
	max := 100    // Valor máximo del número aleatorio generado
	arr := generateRandomArray(size, min, max)

	// Copiamos el arreglo generado para no medir el tiempo de generación
	arrCopy := make([]int, len(arr))
	copy(arrCopy, arr)

	// fmt.Println("Arreglo original:", arr)

	// Medición del tiempo de ejecución
	startTime := time.Now()
	selectionSort(arrCopy)
	endTime := time.Now()

	// fmt.Println("Arreglo ordenado:", arrCopy)

	// Calculamos el tiempo de ejecución
	elapsedTime := endTime.Sub(startTime).Milliseconds()
	fmt.Printf("Tiempo de ejecución: %d milisegundos\n", elapsedTime)
	// elapsedTime := endTime.Sub(startTime).Seconds()
	// fmt.Printf("Tiempo de ejecución: %.8f segundos\n", elapsedTime)
}
