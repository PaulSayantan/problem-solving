package bob

import (
	"regexp"
	"strings"
)

// Hey : returns baby response
func Hey(remark string) string {
	remark = strings.TrimSpace(remark)

	switch {
	case isUppercase(remark) && isQuestion(remark):
		return "Calm down, I know what I'm doing!"
	case isUppercase(remark):
		return "Whoa, chill out!"
	case isQuestion(remark):
		return "Sure."
	case isSilent(remark):
		return "Fine. Be that way!"
	default:
		return "Whatever."
	}
}

func isUppercase(input string) bool {
	hasLetters := regexp.MustCompile(`[a-zA-Z]`)
	return strings.ToUpper(input) == input && hasLetters.MatchString(input)
}

func isQuestion(input string) bool {
	return strings.HasSuffix(input, "?")
}

func isSilent(input string) bool {
	notAlphanumeric := regexp.MustCompile(`^[^a-zA-Z0-9!?]+[^a-zA-Z0-9!?.]]$`)
	return notAlphanumeric.MatchString(input) || len(input) == 0
}
