nums = [1, 2, 3, 2, 5, 4]

prefix = [0]
for n in nums:
    prefix.append(prefix[-1] + n)

left, right = 2, 4
print(prefix)
print(prefix[right + 1] - prefix[left])