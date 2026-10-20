nums = [1]

bestEnding = nums[0]
ans = nums[0]

for i in range(len(nums)):
    v1 = bestEnding + nums[i]
    v2 = nums[i]
    bestEnding = max(v1, v2)
    ans = max(bestEnding, ans)
print(ans)