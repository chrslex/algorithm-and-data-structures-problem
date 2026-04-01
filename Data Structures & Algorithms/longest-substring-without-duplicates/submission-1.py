class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        res = 0
        n = len(s)
        a = ord('a')
        word_count = {}


        while r < n:
            word_count[s[r]] = word_count.get(s[r],0) + 1
            while word_count.get(s[r]) > 1:
                word_count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        
        return res