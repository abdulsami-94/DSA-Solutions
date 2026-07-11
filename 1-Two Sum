nums = [2,7,11,15]
target = 9
res = {}
seen = {}
for i , num in enumerate(nums):
    complement = target - num
    if complement in seen:
        res = [seen[complement], i]
    seen[num] = i


print(res)