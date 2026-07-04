nums = [2,3,1,2,4,3]
target = 7

l = 0 
total = 0
min_len = float('-inf')

for r in range(len(nums)):
    total += nums[r]
    while total >= target:
        min_len = min(total, r - l + 1)
        total -= nums[l]
        l += 1
print(min_len)