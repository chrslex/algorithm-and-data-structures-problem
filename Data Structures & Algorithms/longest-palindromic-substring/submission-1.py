class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resLen = 1
        startPos = 0

        dp = [[True for _ in range(n)] for _ in range(n)]

        for i in range(n-2, -1,-1):
            for j in range(i+1, n):
                # assume char more than 1 char is not palindrome
                dp[i][j] = False

                # if palindrome, check inner string also palindrome
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]

                    # if inner string is palindrome, eval length
                    if dp[i][j] and (j-i+1) > resLen:
                        startPos = i
                        resLen = j-i+1

        return s[startPos:startPos+resLen] 