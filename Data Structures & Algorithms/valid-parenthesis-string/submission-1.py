class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_a, stack_b = [], []
        for i in range(len(s)):
            if s[i] == "(":
                stack_a.append(i)
            elif s[i] == "*":
                stack_b.append(i)
            else:
                if stack_a:
                    stack_a.pop()
                elif stack_b:
                    stack_b.pop()
                else:
                    return False
        
        while stack_a and stack_b:
            if stack_a.pop() > stack_b.pop():
                return False
        return stack_a == [] 
        