import unittest
import time

''' Simplified Solution '''
def timeConversion(mytime: str) -> str:
    return str(time.strftime('%H:%M:%S', time.strptime(mytime, '%I:%M:%S%p')))


''' Descriptive Solution '''
# def timeConversion(time: str) -> str:
#     h, m, s = map(int, time[:-2].split(':'))
#     am_pm = time[-2:]
#     h = h % 12 + (am_pm.upper() == 'PM') * 12
#     return (('%02d:%02d:%02d') % (h, m, s))

class timeConversionTest(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(timeConversion('07:05:45PM'), '19:05:45')
    def testcase2(self):
        self.assertEqual(timeConversion('12:00:00AM'), '00:00:00')
    def testcase3(self):
        self.assertEqual(timeConversion('04:59:59AM'), '04:59:59')
    def testcase4(self):
        self.assertEqual(timeConversion('11:59:59PM'), '23:59:59')


if __name__ == "__main__":
    unittest.main()
