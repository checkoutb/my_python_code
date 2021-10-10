

# import 
# import 
# import 


        # for i,char in enumerate(s):
        #     if char in seen and start<=seen[char]:
        #         start = seen[char] + 1
        #     length=i-start+1
        #     maxlength = max(maxlength,length)
        #     seen[char]=i
# 不需要 内部的 for/while 了

        # for j in range(n):
        #     if s[j] in char_index:
        #         i = max(char_index[s[j]], i)
        #     max_length = max(max_length, j - i + 1)
        #     char_index[s[j]] = j + 1

# for i in range(len(s)):


# Runtime: 107 ms, faster than 30.28% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.3 MB, less than 53.67% of Python3 online submissions for Longest Substring Without Repeating Characters.
class LT0003:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map2 = {}
        st = 0
        ans = 0
        idx = -1
        for ch in s:
            idx += 1
            if ch in map2 and map2[ch] != -1:
                while st <= map2[ch]:
                    map2[s[st]] = -1
                    st += 1
            map2[ch] = idx
            ans = max(ans, (idx - st + 1))
        return ans


if __name__ == '__main__':
    sol = LT0003()
    # s = "abcabcbb"
    # s = "bbbbb"
    # s = "pwwkew"
    s = ""

    print(sol.lengthOfLongestSubstring(s))

    