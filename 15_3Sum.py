a = [1, 1, 1, 2, 2, 3, 3, 3]


i = 0
l = i + 1
r = len(a) - 1
target = 0
res = []

while l < r:
    sum = a[l] + a[r]

    if sum == target:
        res.append((a[l], a[r]))
        l += 1
        r -= 1
        while l < j and a[l] == a[l - 1]:
            l += 1
        while l < r and a[r] == a[r + 1]:
            r -= 1
    elif sum > target:
        r -= 1
    else:
        l += 1

print(res)



