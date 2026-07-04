a = [1,2,3,0,0,0]
b = [2,5,6]
m = 3
n = 3

i = m -1
j = n - 1
k = m + n - 1

while i >= 0 and j >= 0:
    if a[i] > b[j]:
        a[k] = a[i]
        i -= 1
    else:
        a[k] = b[j]
        j -= 1
    k -= 1

while j >= 0:
    a[k] = b[j]
    j -= 1
    k -= 1

print(a)


'''
# 1 POINTER O(n)
i = 0
j = len(a)
result = []
while i < j:
    if a[i] < b[i]:
        result.append(a[i])
        result.append(b[i])
    else:
        result.append(b[i])
        result.append(a[i])
    i += 1
'''