class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        word_count = {}
        
        for r in range(len(s)):
            word_count[s[r]] = word_count.get(s[r], 0) + 1

            while (r-l+1) - max(word_count.values()) > k :
                word_count[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
        return res

