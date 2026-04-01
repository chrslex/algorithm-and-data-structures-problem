class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        d = deque()
        for char in s:
            if char in "([{":
                d.append(char)
            else:
                if len(d) == 0:
                    return False
                open_bracket = d.pop()
                check = pMap[open_bracket]
                if check != char:
                    return False
        return len(d) == 0