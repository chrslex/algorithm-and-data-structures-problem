class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        lp, rp = 0, 0
        res = 0

        m = {}

        while rp < n:
            m[s[rp]] = m.get(s[rp], 0) + 1

            while m[s[rp]] > 1:
                m[s[lp]] -= 1
                lp += 1
            
            res = max(res, rp-lp+1)
            rp += 1
        
        return res