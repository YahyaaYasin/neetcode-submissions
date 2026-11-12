class Solution:
    def isPalindrome(self, s: str) -> bool:

        while s and not s[0].isalnum():
            s = s[1:]

        while s and not s[-1].isalnum():
            s = s[:-1]

        if len(s) <= 1:
            return True

        if s[0].lower() != s[-1].lower():
            return False

        return self.isPalindrome(s[1:-1])
        