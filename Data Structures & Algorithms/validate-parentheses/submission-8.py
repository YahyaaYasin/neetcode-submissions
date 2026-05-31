
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        openers = "([{"
        closers = ")]}"

        for char in s:
            if char in openers:
                stack.append(char)
            elif char in closers:
                if not stack:
                    return False
                else:
                    latest_opening = stack.pop()
                    if openers.find(latest_opening) != closers.find(char):
                        return False
        return stack == []