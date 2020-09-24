_, k = (int(k) for k in input().split())
arr = [int(x) for x in input().split()]
b_charged = int(input())
b_actual = (sum(arr) - arr[k]) // 2
if b_charged <= b_actual:
    print("Bon Appetit")
else:
    print(b_charged - b_actual)