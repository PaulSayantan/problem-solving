import datetime

actual = datetime.date(*[int(x) for x in input().split()][::-1])
expected = datetime.date(*[int(x) for x in input().split()][::-1])
fine = 0
days = actual.day - expected.day 
months = actual.month - expected.month
years = actual.year - expected.year

# before a year
if years < 0:
    fine = 0
# after a year
elif years > 0:
    fine = 10000
# same year previous month 
elif years == 0 and months < 0:
    fine = 0
# same year after month
elif years == 0 and months > 0:
    fine = months * 500
# same year same month after day
elif years == 0 and months == 0 and days > 0:
    fine = days * 15
# same year same month on/before day
else:
    fine = 0

if fine > 0:
    print(fine)
else:
    print(0)