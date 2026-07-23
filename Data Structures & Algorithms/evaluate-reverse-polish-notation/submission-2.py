class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(int(t))
                print(stack)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if t == '+':
                    ans = num1 + num2
                elif t == '-':
                    ans = num1 - num2
                elif t == '*':
                    ans = num1 * num2
                else:
                    ans = int(num1 / num2)
                stack.append(ans)
                print(stack)

        return stack[-1]