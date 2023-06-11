def generateParenthesis(n: int) -> list[str]:
        stack = []
        result = []
        def backtracking(open, close, cur_string):
            if len(cur_string) == n*2:
                result.append("".join(stack))
                return
            if open < n:
                cur_string.append("(")
                backtracking(open + 1, close, cur_string)
                cur_string.pop()
            if close < n and close < open:
                cur_string.append(")")
                backtracking(open, close + 1, cur_string)
                cur_string.pop()

        backtracking(0, 0, stack)
        return result

print(generateParenthesis(6))
