"""
Problem:
		Write an algorithm to determine if a number n is happy.

		A happy number is a number defined by the following process:

		   * Starting with any positive integer, replace the number by the sum of the squares of its digits.
		   * Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
		   * Those numbers for which this process ends in 1 are happy.

		Return true if n is a happy number, and false if not.

"""

def isHappy(n: int) -> bool:
	if n == 1:
		return True
	
	squares = set()

	while True:
		temp = 0
		for i in str(n):
			temp += int(i) ** 2
		if temp in squares: return False
		
		n = temp
		squares.add(n)
		if n == 1: return True
		

print(isHappy(19))
print(isHappy(2))