package diffsquares

// SquareOfSum function that calculates the square of the sum of range of numbers
func SquareOfSum(n int) int {
	s := 0
	for i := 0; i <= n; i++ {
		s += i
	}
	return s * s
}

// SumOfSquares function that calculates the sum of squares of range of numbers
func SumOfSquares(n int) (s int) {
	for i := 0; i <= n; i++ {
		s += i * i
	}
	return
}

// Difference = SquareofSum - SumOfSquares
func Difference(n int) int {
	return SquareOfSum(n) - SumOfSquares(n)
}
