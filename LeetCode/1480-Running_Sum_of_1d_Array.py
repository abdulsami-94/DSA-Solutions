# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

nums = [1, 2, 3, 4]
pre = [0] * len(nums)
pre[0] = nums[0]

for i in range(1, len(nums)):
    pre[i] = pre[i-1] + nums[i]

print(pre)