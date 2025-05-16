class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        directories = path.split('/')
        for directory in directories:
            # Duplicate / in the `path` string will be split as empty strings
            if not directory:
                continue # Empty string, do nothing

            if directory == '.':
                    continue # Current directory -- do nothing
            elif directory == '..':
                if stack: # Previous directory -- pop current directory off the stack
                    stack.pop()
            else: # A valid directory -- push it onto the stack prefixed by a /
                stack.append('/' + directory)
        
        # If the stack is empty we are at the root directory
        return '/' if not stack else "".join(stack)
