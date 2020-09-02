_, x = (int(x) for x in input().split())
zipper = list()
for _ in range(x):
    marks = [float(x) for x in input().split()]
    zipper += [marks]
for subs in zip(*zipper):
    print('{:.1f}'.format(sum(subs) / x))