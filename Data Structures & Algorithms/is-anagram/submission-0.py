class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)

        if(ns != nt):
            return False
        chars = [0] * 26

        for i in range(nt):
            chars[ord(s[i]) - 97] += 1
            chars[ord(t[i]) - 97] -= 1

        for i in range(len(chars)):
            if(chars[i] != 0):
                return False

        return True