package hamming

import (
	"errors"
)

// Distance function to return Hamming Distance between two DNA strands
func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return 0, errors.New("Cannot accquire Hamming Distance")
	}

	dist := 0
	for i := 0; i < len(a); i++ {
		if a[i] == b[i] {
			dist++
		}
	}
	return dist, nil
}
