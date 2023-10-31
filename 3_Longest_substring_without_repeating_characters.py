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

