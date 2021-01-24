package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d", &n)

	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &arr[i])
	}

	max, min := arr[0], arr[0]
	maxCount, minCount := 0, 0
	for i := 1; i < n; i++ {
		if arr[i] > max {
			max = arr[i]
			maxCount++
		}
		if arr[i] < min {
			min = arr[i]
			minCount++
		}
	}

	fmt.Println(maxCount, minCount)
}
