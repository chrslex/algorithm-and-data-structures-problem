class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)

        if ns != nt:
            return False
        
        counter = [0 for _ in range(26)]

        for i in range(nt):
            counter[ord(s[i]) - 97] += 1
            counter[ord(t[i]) - 97] -= 1
        
        for i in range(len(counter)):
            if counter[i] != 0:
                return False
        return True