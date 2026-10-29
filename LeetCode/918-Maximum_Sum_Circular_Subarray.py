nums = [5, -2, -3, -6, 3]
#answers will be 5+3=8

total = 0
curMax = curMin = 0
maxSum = minSum = nums[0]

for x in nums:
    curMax = max(curMax + x, x)
    maxSum = max(maxSum, curMax)

    curMin = min(curMin + x, x)
    minSum = min(minSum, curMin)

    total += x

print(max(maxSum, total - minSum))
    