class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dct = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for i in s:
            if i in dct:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i != dct[stack.pop()]:
                    return False
            
        return len(stack) == 0