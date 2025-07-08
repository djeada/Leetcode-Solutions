class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
        ')' : '(', 
        '}' : '{', 
        ']' : '['
        }

        for character in s:
            if character in parentheses:
                if stack and stack[-1] == parentheses[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)

        return len(stack) == 0
        
