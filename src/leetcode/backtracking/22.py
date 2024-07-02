class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        stack = []
        def backtrack(opening, closing):
            # Base case
            if opening == n and closing == n:
                res.append("".join(stack))
                return

            # Actions
            # 2 decisions - either close a paren, or add a new open paren

            # Action 1 - if there are less than `n` opening parenthesis, open another one
            if opening < n:
                stack.append('(')
                backtrack(opening + 1, closing)
                # Undo before taking the next action
                stack.pop()

            # Action 2 - add a closing parenthesis if allowed
            if closing < opening:
                stack.append(')')
                backtrack(opening, closing + 1)
                # Undo before taking the next action
                stack.pop()


        backtrack(0, 0)
        return res
