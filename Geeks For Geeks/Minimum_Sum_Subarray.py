arr = [3,-4, 2,-3,-1, 7,-5]

count = arr[0]
mini = arr[0]

for i in range(1, len(arr)):
    count = min(arr[i], count + arr[i])
    mini = min(mini, count)

print(mini)