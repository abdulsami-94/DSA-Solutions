nums = [-2, 3, -4]

minEnd = nums[0]
maxEnd = nums[0]
res = nums[0]

for i in range(len(nums)):
    v1 = nums[i]
    v2 = minEnd * nums[i]
    v3 = maxEnd * nums[i]

    minEnd = min(v1, min(v2, v3))
    maxEnd = max(v1, max(v2, v3))
    res = max(res, maxEnd)

print(res)