def lengthOfLongestSubstring(s: str):
    pos = {}
    longest = i = 0

    for j, c in enumerate(s):
        if c in pos:
            i = max(pos[c], i)

        pos[c] = j + 1
        longest = max(longest, j - i + 1)

    return longest
