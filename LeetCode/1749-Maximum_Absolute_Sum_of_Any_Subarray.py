nums = [1,-3,2,3,-4]

maxEnd = minEnd = 0
res = 0

for x in nums:
    maxEnd = max(maxEnd + x, 0)
    minEnd = min(minEnd + x, 0)
    res = max(res, maxEnd, abs(minEnd))

print(res)