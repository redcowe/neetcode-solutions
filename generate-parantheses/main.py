def generateParenthesis(n: int) -> list[str]:
        #there can only be n number of open and clothes parantheses
        #can only add as many open parantheses are we want
        #there can never be more close paranthese than open paranthese
        answer = []
        def backtracking(cur_string, left_count, right_count):
            if len(cur_string) == 2 * n:
                answer.append("".join(cur_string))
                return
            if left_count < n:
                cur_string.append("(")
                backtracking(cur_string, left_count + 1, right_count)
                cur_string.pop()
            if right_count < left_count:
                cur_string.append(")")
                backtracking(cur_string, left_count, right_count + 1)
                cur_string.pop()
        backtracking([], 0, 0)
        return answer

generateParenthesis(3)
