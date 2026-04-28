class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        res = 0
        lp, rp = 0, 0

        while rp < len(s):
            d[s[rp]] = d.get(s[rp], 0) + 1
            while d[s[rp]] > 1:
                d[s[lp]] -= 1
                lp += 1
            res = max(res, rp - lp + 1)
            rp += 1
        
        return res