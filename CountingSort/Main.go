package main

import (
	"fmt"
	"math/rand"
	"time"
)

func findMax(arr []int) int {
	var temp int

	temp = arr[0]

	for _, e := range arr {
		if temp < e {
			temp = e
		}
	}

	return temp
}

func makeRange(min, max int) []int {
	a := make([]int, max-min+1)
	for i := range a {
		a[i] = 0
	}
	return a
}

func countingSort(arr []int) []int {
	// generate array from min to max
	//todo: wie unten lösen
	counter := makeRange(0, findMax(arr))

	// count
	for _, e := range arr {
		counter[e] += 1
	}

	// add prev val to curr
	for i := 1; i < len(counter); i++ {
		counter[i] += counter[i-1]
	}

	// copy to correct pos
	res := make([]int, len(arr))

	for i := 0; i < len(arr); i++ {
		e := arr[i]         // elem to add
		t := counter[e] - 1 // target pos

		res[t] = e
		counter[e] = counter[e] - 1
	}

	return res
}

func printArr(arr []int) {
	for i, e := range arr {
		println(i, ":", e)
	}
}

func main() {
	//Provide seed
	rand.Seed(time.Now().Unix())

	//Generate a random array of length n
	// fmt.Println(rand.Perm(10))
	// fmt.Println(rand.Perm(10))
	// data := []int{ 5, 1, 9, 51, 9, 2 }
	x := []int{100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 1}
	var out []float64
	for _, s := range x {
		data := rand.Perm(s)
		start := time.Now()

		countingSort(data)

		elapsed := time.Since(start)
		out = append(out, elapsed.Seconds()*1000)
	}
	for _, v := range out {
		fmt.Printf("%v\n", v)
	}
	// println(elapsed.Seconds())
	// data := rand.Perm(100)

	// // println("data")
	// // printArr(data)

	// start := time.Now()

	// countingSort(data)

	// elapsed := time.Since(start)

	// println(elapsed.Seconds())

	// println("sorted")
	// printArr(sorted)
}
