package main

import "fmt"

func sum(arr []int) int {
	val := 0
	for _, elem := range arr {
		val += elem
	}
	return val
}

// m squares summed up to d
func count(bar []int, n int, m int, d int) int {
	count := 0
	for i := 0; i <= n-m; i++ {
		if sum(bar[i:i+m]) == d {
			count += 1
		}
	}
	return count
}

func read_arr(n int) ([]int, error) {
	arr := make([]int, n)
	for i := range arr {
		_, err := fmt.Scan(&arr[i])
		if err != nil {
			return arr[:i], err
		}
	}
	return arr, nil
}

func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	var n, d, m int
	fmt.Scanf("%v", &n)
	bar, _ := read_arr(n)
	fmt.Scanf("%v", &d)
	fmt.Scanf("%v", &m)
	fmt.Println(count(bar, n, m, d))
}
