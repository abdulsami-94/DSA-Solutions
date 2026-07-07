nums = [10, 5, 2, 6]
k = 100

l = 0
res = 0
product = 1

for r in range(len(nums)):
    product *= nums[r]

    while l <= r and product >= k:
        product = product // nums[l]
        l += 1
    res += (r - l + 1)

print(res)
        