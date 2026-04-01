class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l, r = 0,0
        n = len(s)
        word_counter = {}

        while r < n:
            word_counter[s[r]] = word_counter.get(s[r], 0) + 1
            while (r-l+1) - max(word_counter.values()) > k:
                word_counter[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res
