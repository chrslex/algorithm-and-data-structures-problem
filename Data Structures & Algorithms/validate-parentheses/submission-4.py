class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        st = deque()

        for ch in s:
            if ch in "({[":
                st.append(ch)
            else:
                if not st:
                    return False
                close_bracket_check = m[st.pop()]
                if ch == close_bracket_check:
                    continue
                else:
                    return False
        return len(st) == 0