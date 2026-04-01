class Solution:
    def longestPalindrome(self, s: str) -> str:
        start_pos = 0
        max_len = 1
        n = len(s)

        dp = [[True] * n for _ in range(n)]

        for i in range(n-2, -1,-1):
            for j in range(i+1, n):
                dp[i][j] = False

                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]

                    if dp[i][j] and max_len < j-i+1:
                        max_len = max(max_len, j-i+1)
                        start_pos = i
                
        return s[start_pos:start_pos+max_len]