class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0,0
        n = len(s)
        word_counter = {}

        while r < n:
            # if not s[r].isalnum():
            #     r -= 1
            #     continue
            # elif not s[l].isalnum():
            #     l += 1
            #     continue
            
            word_counter[s[r]] = word_counter.get(s[r], 0) + 1
            while word_counter[s[r]] > 1:
                word_counter[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res