nums = [-2,1,-3,4,-1,2,1,-5,4]

sum = 0
maxi = nums[0]

for i in range(len(nums)):

    sum = sum + nums[i]

    if sum > maxi:
        maxi = sum 

    if sum < 0:
        sum = 0

        
        

print(maxi)