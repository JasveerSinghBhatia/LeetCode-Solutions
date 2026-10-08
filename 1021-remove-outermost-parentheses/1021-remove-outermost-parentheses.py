class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt = 0
        result =""
        for ch in s:
            if ch == '(':
                if cnt != 0 :
                    result += ch
                cnt += 1
            else:
                cnt -= 1
                if(cnt != 0 ):
                    result += ch
        return result