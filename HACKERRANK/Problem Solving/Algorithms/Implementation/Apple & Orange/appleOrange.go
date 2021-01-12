package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
	"unicode"
)

var (
	r *Reader
)

type Reader struct {
	data []string
	p    int
}

func (r *Reader) spaceMap(str string) string {
	return strings.Map(func(r rune) rune {
		if unicode.IsSpace(r) {
			return ' '
		}
		return r
	}, str)
}

func (r *Reader) ReadAll() {
	bytes, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		panic(err)
	}
	r.data = strings.Split(r.spaceMap(string(bytes)), " ")
}

func (r *Reader) Next() (s string) {
	s = r.data[r.p]
	r.p += 1

	return s
}

func (r *Reader) NextInt() (n int) {
	n, err := strconv.Atoi(r.data[r.p])
	if err != nil {
		panic(err)
	}
	r.p += 1
	return
}

func init() {
	r = &Reader{}
	r.ReadAll()
}

func main() {
	s := r.NextInt()
	t := r.NextInt()

	a := r.NextInt()
	b := r.NextInt()

	m := r.NextInt()
	n := r.NextInt()

	isHitted := func(x int) bool {
		if s <= x && x <= t {
			return true
		}
		return false
	}

	appleCount := 0

	for ; m > 0; m-- {
		apple := r.NextInt()
		appleX := a + apple

		if isHitted(appleX) {
			appleCount++
		}
	}

	orangeCount := 0

	for ; n > 0; n-- {
		orange := r.NextInt()
		orangeX := b + orange

		if isHitted(orangeX) {
			orangeCount++
		}
	}

	fmt.Println(appleCount)
	fmt.Println(orangeCount)
}
