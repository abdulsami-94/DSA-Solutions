nums = [2, 0, 2, 1, 1, 0]
'''
# Brute Force uses 2 passes

zero = 0
one = 0
two = 0

i = 0 

for i in range(len(nums)):
    if nums[i] == 0:
        zero += 1
    elif nums[i] == 1:
        one += 1
    else:
        two += 1

for i in range(len(nums)):
    if i < zero:
        nums[i] = 0
    elif i < zero + one:
        nums[i] = 1
    else:
        nums[i] = 2
'''

# Dutch Flag Algorith Uses 1 Passes

low, mid, high = 0, 0 , len(nums) - 1

while mid <= high:
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
    elif nums[mid] == 1:
        mid += 1
    else:
        nums[mid], nums[high] = nums[high],nums[mid]
        high -= 1            
        
print(nums)