def arrayUpdate(nums: list, target: int) -> int:
    if nums[0] >= target:
        return 0
    return target - min(nums)

if __name__ == "__main__":
    res = list()
    array_len, tar = (int(x) for x in input().split())
    for _ in range(int(input())):
        res.append(arrayUpdate([int(x) for x in input().split()], tar))
    [print(r) for r in res]