length = int(input())
scores = [int(x) for x in input().split()]
high_score, low_score = scores[0], scores[0]
highcount, lowcount = 0, 0
for i in range(1, length):
    if high_score < scores[i]:
        high_score = scores[i]
        highcount += 1
    
    if low_score > scores[i]:
        low_score = scores[i]
        lowcount += 1

print(highcount, lowcount)