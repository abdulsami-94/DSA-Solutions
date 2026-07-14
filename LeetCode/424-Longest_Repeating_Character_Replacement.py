s = "ABABBA"
k = 2

longest = 0
seen = {}
l = 0

for r in range(len(s)):

    seen[s[r]] = seen.get(s[r], 0) + 1

    max_val = max(seen.values())
        
    if (r - l) + 1 - max_val <= k :
        longest = max(longest, (r - l ) + 1)
    else:
        seen[s[l]] -= 1
        if seen[s[l]] == 0:
            del seen[s[l]]
        l += 1

print(longest)

        