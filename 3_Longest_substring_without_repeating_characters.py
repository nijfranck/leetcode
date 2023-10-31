def lengthOfLongestSubstring(s: str) -> int:
        mydict = {}
        counter = 0
        max_counter = 0
        len_s = len(s)
        i = 0
        while i < len_s:
            if s[i] not in mydict:
                mydict[s[i]] = i
                counter += 1
                if counter > max_counter:
                    max_counter = counter
            else:
                counter = 1
                i = mydict[s[i]] + 1
                mydict = {}
                mydict[s[i]] = i
            i+=1
        
        return max_counter

# Runtime
# 395ms
# Beats 9.64%of users with Python3

# Memory
# 16.30MB
# Beats 85.45%of users with Python3

def lengthOfLongestSubstring(s: str) -> int:
    mydict = {}
    start = 0
    max_length = 0

    for end in range(len(s)):
        if s[end] in mydict:
            start = max(start, mydict[s[end]] + 1)
        mydict[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length

# Runtime
# 60ms
# Beats 62.62%of users with Python3

# Memory
# 16.40MB
# Beats 54.48%of users with Python3


def lengthOfLongestSubstring(s: str) -> int:
    index = [-1] * 128  # ASCII size
    start = 0
    max_length = 0

    for end in range(len(s)):
        start = max(start, index[ord(s[end])] + 1)
        index[ord(s[end])] = end
        max_length = max(max_length, end - start + 1)

    return max_length


def lengthOfLongestSubstring(s: str) -> int:
    index = [-1] * 26  # only lowercase English letters
    start = 0
    max_length = 0

    for end in range(len(s)):
        start = max(start, index[ord(s[end]) - ord('a')] + 1)
        index[ord(s[end]) - ord('a')] = end
        max_length = max(max_length, end - start + 1)

    return max_length