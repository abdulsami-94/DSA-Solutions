nums = [1,12,-5,-6,50,3]
k = 4

window_sum = sum(nums[:k])
max_avg = window_sum

for l in range(k, len(nums)):
    window_sum += nums[l]
    window_sum -= nums[l - k]


    if window_sum > max_avg:
        max_avg = window_sum

print(max_avg)
#print(f"{max_avg/k}")
    