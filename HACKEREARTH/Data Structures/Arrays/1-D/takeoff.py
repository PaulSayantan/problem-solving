'''Better Solution'''
def solution1():
    result = list()
    for _ in range(int(input())):
        N, p, q, r = (int(x) for x in input().split())
        if p == q or p == r or q == r:
            result.append(0)
            break
        count = 0
        for i in range(2, N+1):
            if i % p == 0 and i % q != 0 and i % r != 0:
                count += 1
            if i % p != 0 and i % q == 0 and i % r != 0:
                count += 1
            if i % p != 0 and i % q != 0 and i % r == 0:
                count += 1
        result.append(count)
    [print(r) for r in result]


'''Partially Accepted'''
def solution2():
    result = list()
    for _ in range(int(input())):
        N, p, q, r = (int(x) for x in input().split())
        if p == q or p == r or q == r:
            result.append(0)
            break
        nums = set()
        i = 1
        tp, tq, tr = p, q, r
        while tp <= N or tq <= N or tr <= N:
            if tp <= N:
                if tp in nums:
                    nums.remove(tp)
                else:
                    nums.add(tp)
            if tq <= N:
                if tq in nums:
                    nums.remove(tq)
                else:
                    nums.add(tq)
            if tr <= N:
                if tr in nums:
                    nums.remove(tr)
                else:
                    nums.add(tr)
            i += 1
            tp = i * p
            tq = i * q
            tr = i * r

        result.append(len(nums))

    [print(r) for r in result]