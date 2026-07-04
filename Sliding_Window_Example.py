'''
a = [1, 0, 3, 5, 2, 1, 4]

i, j, k = 0, 1, 2
best = float('-inf')

while k <= len(a) - 1:
    current = a[i] + a[j] + a[k]
    
    if current > best:
        best = current
    i += 1
    j += 1
    k += 1
print(best)
'''

# Sliding Window Example

a = [1, 0, 3, 5, 2, 1, 4]

window_sum = a[0] + a[1] + a[2]
best = window_sum

for i in range(3, len(a)):
    window_sum += a[i]
    window_sum -= a[i -3]

    if window_sum > best:
        best = window_sum
print(best)