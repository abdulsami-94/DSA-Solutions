nums = [2,3,-2,4]

res = max(nums)
curMax, CurMin = 1, 1

for n in nums:
    if n == 0:
        curMax, CurMin = 1, 1
        continue
    tmp = curMax * n
    curMax = max(n * curMax, n * CurMin , n)
    curMin = min(tmp, n * CurMin , n)
    res = max(res, curMax, CurMin)
print(res)