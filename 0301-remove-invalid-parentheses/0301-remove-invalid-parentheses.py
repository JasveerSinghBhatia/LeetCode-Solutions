class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        n = len(s)
        st = set()
        maxLen = 0

        def solve(i, curr, cnt):
            nonlocal maxLen

            # More ')' than '('
            if cnt < 0:
                return

            # Reached the end
            if i == n:
                if cnt == 0:
                    result = "".join(curr)

                    if len(result) > maxLen:
                        maxLen = len(result)
                        st.clear()

                    if len(result) == maxLen:
                        st.add(result)

                return

            # Non-parenthesis character
            if s[i] != '(' and s[i] != ')':
                curr.append(s[i])

                solve(i + 1, curr, cnt)

                curr.pop()
                return

            # Option 1: Keep the parenthesis
            curr.append(s[i])

            if s[i] == '(':
                solve(i + 1, curr, cnt + 1)
            else:
                solve(i + 1, curr, cnt - 1)

            curr.pop()

            # Option 2: Remove the parenthesis
            solve(i + 1, curr, cnt)

        curr = []

        solve(0, curr, 0)

        return list(st)