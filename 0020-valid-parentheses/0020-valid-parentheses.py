class Solution:
    def isValid(self, s: str) -> bool:
        #defining a stack
        stack = []
        pairs = {']' : '[', '}' : '{', ')' : '('}

        for char in s:
            if char in "[{(" :
                stack.append(char)
            
            elif char in "]})":
                if not stack or stack[-1] != pairs[char]:  #stack[-1] is accessing the top most element of stack without removing it
                    return False
                
                stack.pop()

        return len(stack) == 0