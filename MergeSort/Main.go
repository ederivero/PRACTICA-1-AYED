package main

import (
	"fmt"
	"time"
)

func merge(arr []int, left int, mid int, right int) {
	n1 := mid - left + 1
	n2 := right - mid

	leftArr := make([]int, n1)
	rightArr := make([]int, n2)

	for i := 0; i < n1; i++ {
		leftArr[i] = arr[left+i]
	}

	for j := 0; j < n2; j++ {
		rightArr[j] = arr[mid+1+j]
	}

	i, j, k := 0, 0, left

	for i < n1 && j < n2 {
		if leftArr[i] <= rightArr[j] {
			arr[k] = leftArr[i]
			i++
		} else {
			arr[k] = rightArr[j]
			j++
		}
		k++
	}

	for i < n1 {
		arr[k] = leftArr[i]
		i++
		k++
	}

	for j < n2 {
		arr[k] = rightArr[j]
		j++
		k++
	}
}

func mergeSort(arr []int, left int, right int) {
	if left < right {
		mid := (left + right) / 2
		mergeSort(arr, left, mid)
		mergeSort(arr, mid+1, right)
		merge(arr, left, mid, right)
	}
}

func main() {
	arr := []int{1, 2, 3}
	inicio := time.Now()
	mergeSort(arr, 0, len(arr)-1)
	fin := time.Now()
	tiempoEjecucion := float64(fin.Sub(inicio).Seconds())
	fmt.Printf("Tiempo de ejecución: %.8f", tiempoEjecucion)
}
