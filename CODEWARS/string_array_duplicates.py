import unittest
from typing import List

def duplicates(arr: List[str]) -> List[str]:
    for pos in range(len(arr)):
        string = arr[pos]
        new_string = [string[0]]
        for char in string:
            if new_string[-1] == char:
                continue
            else:
                new_string.append(char)
        _ = arr.pop(pos)
        arr.insert(pos, ''.join(new_string))
    
    return arr

class duplicatesTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(duplicates(["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]),['codewars','picaniny','hubububo'])
    def test2(self):
        self.assertEqual(duplicates(["abracadabra","allottee","assessee"]),['abracadabra','alote','asese'])
    def test3(self):
        self.assertEqual(duplicates(["kelless","keenness"]), ['keles','kenes'])
    def test4(self):
        self.assertEqual(duplicates(["Woolloomooloo","flooddoorroommoonlighters","chuchchi"]), ['Wolomolo','flodoromonlighters','chuchchi'])
    def test5(self):
        self.assertEqual(duplicates(["adanac","soonness","toolless","ppellee"]), ['adanac','sones','toles','pele'])

if __name__ == "__main__":
    unittest.main()