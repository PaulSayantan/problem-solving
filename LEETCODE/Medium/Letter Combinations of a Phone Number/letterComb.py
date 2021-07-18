"""
Problem:
		Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
		that the number could represent. Return the answer in any order.

"""

from itertools import product
from typing import List

digit_map = {
				'2': ['a','b','c'], '3': ['d','e','f'], 
				'4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'], 
				'7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z']
			}

def letterCombinations(digits: str) -> List[str]:
	if digits == '' or digits == '1':
		return []

	if len(digits) == 1: 
		return digit_map[digits]

	characters = []
	for digit in digits:
		characters.append(digit_map[digit])

	return [''.join(prod) for prod in product(*characters)]
