"""
Problem:

		Given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

	Letters are case sensitive, so "a" is considered a different type of stone from "A".

"""

def numJewelsInStones(jewels: str, stones: str) -> int:
	return len(stones) - len(stones.strip(jewels))

print(numJewelsInStones(jewels = "z", stones = "ZZ"))			# Output: 0
print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))		# Output: 3