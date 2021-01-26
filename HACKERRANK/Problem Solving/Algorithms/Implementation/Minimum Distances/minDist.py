import unittest
from typing import List
from collections import defaultdict

def minimumDistances(arr: List[int], size: int) -> int:
    minDist = 10**5
    position_map = dict()

    position_map = defaultdict(list)
    for pos, item in enumerate(arr):
        position_map[item].append(pos)

    for i in position_map:
        if type(position_map.get(i)) == list and len(position_map.get(i)) > 1:
            dist = position_map.get(i)[1] - position_map.get(i)[0]

            if dist < minDist:
                minDist = dist

    return minDist if minDist != 10**5 else -1


class TestMinDist(unittest.TestCase):
    def test_min_dist_1(self):
        self.assertEqual(minimumDistances([3, 2, 1, 2, 3], 5), 2)
    
    def test_min_dist_2(self):
        self.assertEqual(minimumDistances([7, 1, 3, 4, 1, 7], 6), 3)

if __name__ == '__main__':
    unittest.main()