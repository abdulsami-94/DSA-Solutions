s = "aabacbebebe"
k = 3

left = 0
longest = -1
seen = {}

for right in range(len(s)):
    if s[right] in seen:
        seen[s[right]] += 1
    else:
        seen[s[right]] = 1

    while len(seen) > k:
        seen[s[left]] -= 1

        if seen[s[left]] == 0:
            del seen[s[left]]
        left += 1
    if len(seen) == k:
        longest = max(longest, right - left + 1)


print(longest)
    
