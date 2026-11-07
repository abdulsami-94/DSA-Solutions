# nums = [1,7,3,6,5,6] 
# ans = 3
# nums = [1, 2, 3] 
# ans = -1
nums = [2, 1, -1]

total = sum(nums)
leftSum = 0

ans = -1

for i in range(len(nums)):
    rightSum = total - leftSum - nums[i]
    if leftSum == rightSum:
        ans = i 
        break   
    leftSum += nums[i]

print(ans)