arr = [3, 1, 5, 2, 9, 4]

max_ele = arr[0]  # assume first is max
for num in arr:
    if num > max_ele:
        max_ele = num

print("Max element:", max_ele)