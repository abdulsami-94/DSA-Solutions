nums = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]


l = 0
r = 0

for i in range(len(nums)):
    if nums[r] == 0:
        nums[l], nums[r] = nums[r],nums[l]
        l += 1
        r += 1
    else:
        r += 1


print(nums)