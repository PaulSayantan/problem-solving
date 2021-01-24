budget, n_key, n_usb = (int(x) for x in input().split())

key_arr = [int(x) for x in input().split()]
usb_arr = [int(x) for x in input().split()]
max = -1
for i in key_arr:
    for j in usb_arr:
        if max < (i + j) and (i + j) <= budget:
            max = i + j

print(max)