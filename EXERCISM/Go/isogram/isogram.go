package isogram

import (
	"strings"
)

// IsIsogram to check if input string is an Isogram or not
func IsIsogram(input string) (bool, error) {
	input = strings.ToLower(strings.Replace(input, "-", "", -1))
	for i := range input {
		letter := string(input[i])
		if strings.ContainsAny(letter, input[i+1:]) {
			return false, nil
		}
	}

	return true, nil
}
