nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

zeros = 0
longest = 0
l = 0

for r in range(len(nums)):

    if nums[r] == 0:
        zeros += 1

    if zeros <= k:
        longest = max(longest, (r - l) + 1)
    else:
        if nums[l] == 0:
            zeros -= 1
        l += 1


print(longest)