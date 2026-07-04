nums = [-4, -1, 0, 3, 10]
res = []

# for i in range (len(ques)):
#    res.append(ques[i] ** 2)

# res.sort()

# print(res)

'''
# 0(n) but uses extra space
i = 0
pos = []
neg = []    
while i < len(nums):
    if nums[i] < 0:
        pos.append(nums[i] ** 2)
        i += 1
    else:
        neg.append(nums[i] ** 2)
        i += 1
    

pos.reverse()

print(pos)
print(neg)


x = 0
y = 0
res = []

while x < len(pos) and y < len(neg):
    if pos[x] < neg[y]:
        res.append(pos[x])
        x += 1
    else:
        res.append(neg[y])
        y += 1

while x < len(pos):
    res.append(pos[x])
    x += 1

while y < len(neg):
    res.append(neg[y])
    y += 1
    
print(res)

'''

i = 0
j = len(nums) - 1
res=[]

while i <= j:

    if nums[i] ** 2 < nums[j] ** 2:
        res.append(nums[j] ** 2)
        j -= 1
    else:
        res.append(nums[i] ** 2)
        i += 1

res.reverse()
print(res)