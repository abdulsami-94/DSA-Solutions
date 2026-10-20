nums = [-2 , 3 , -4]

count = 0
maxi = nums[0]

for i in range(len(nums)):
    count = count + nums[i]
    if count < maxi:
        count = 0
    
    if count > maxi:
        maxi = count

print(maxi)

