nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

bestEnding = nums[0]
ans = nums[0]

for i in range(len(nums)):
    maxValue = bestEnding + nums[i]
    currentValue = nums[i]
    bestEnding = max(maxValue, currentValue)
    ans = max(bestEnding, ans)
print(ans)