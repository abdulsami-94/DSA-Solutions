nums = [1,-2,0,3]

no_del = nums[0]
one_del = float('-inf')
best = nums[0]

for x in nums[1:]:
    one_del = max(one_del + x, no_del)
    no_del = max(no_del + x, x)
    best = max(best, no_del, one_del)

print(best)