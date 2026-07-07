s = "aabacbebebe"
k = 3

l = 0
longest = 0
Max_len = 3
sett = set()

for r in range(len(s)):
    if s[l] == s[r] or s[r] in sett and len(sett) > Max_len :
        longest += 1
        sett.add(s[r])
    else:
        l += 1
        longest = max(longest, len(sett))
        sett.clear()

print(longest)
    
