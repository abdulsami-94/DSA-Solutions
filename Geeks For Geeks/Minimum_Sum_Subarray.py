arr = [-46, -23, -16, -18, -13, -32, 28, -29, 24, -18, 18, -43, -13, -11, 47, 10, 22, -22]

count = arr[0]
mini = arr[0]

for i in range(1, len(arr)):
    count = min(arr[i], count + arr[i])
    mini = min(mini, count)

print(mini)