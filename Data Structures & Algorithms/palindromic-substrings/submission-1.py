class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        for center in range(n*2-1):
            l = center // 2
            r = (center+1) // 2

            while l >=0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res

        