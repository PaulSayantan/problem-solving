package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func plusMinus(arr []int32) {
	var pos, neg, zero int32
	for i := 0; i < len(arr); i++ {
		if arr[i] > 0 {
			pos++
		} else if arr[i] < 0 {
			neg++
		} else {
			zero++
		}
	}
	fmt.Printf("%.6f\n", float32(pos)/float32(len(arr)))
	fmt.Printf("%.6f\n", float32(neg)/float32(len(arr)))
	fmt.Printf("%.6f\n", float32(zero)/float32(len(arr)))
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1024*1024)

	nTemp, err := strconv.ParseInt(readLine(reader), 10, 64)
	checkError(err)
	n := int32(nTemp)

	arrTemp := strings.Split(readLine(reader), " ")

	var arr []int32

	for i := 0; i < int(n); i++ {
		arrItemTemp, err := strconv.ParseInt(arrTemp[i], 10, 64)
		checkError(err)
		arrItem := int32(arrItemTemp)
		arr = append(arr, arrItem)
	}

	plusMinus(arr)
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
