package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
	"time"
)

func timeConversion(t string) string {
	parsed, _ := time.Parse("3:04:05PM", t)
	return parsed.Format("15:04:05")

}

func main() {
	reader := bufio.NewReader(os.Stdin)
	s, err := readLine(reader)
	checkError(err)
	fmt.Println(timeConversion(s))

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
