nums = [-2,1,-3,4,-1,2,1,-5,4]

count = 0
maxi = nums[0]

for i in range(len(nums)):

    count = count + nums[i]

    if count > maxi:
        maxi = count 

    if count < 0:
        count = 0

        
        

print(maxi)