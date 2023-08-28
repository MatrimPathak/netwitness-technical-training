def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix=strs[0]
    for s in strs[1:]:
        prefix=common_prefix(prefix, s)
    return prefix

def common_prefix(s1, s2):
    i = 0
    while i <len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]

strs1 = ['light', 'live', 'liver']
strs2 = ['light', 'racecar', 'car']

print(longest_common_prefix(strs1))
print(longest_common_prefix(strs2))