class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for char in s:
            if char.isalnum():
                new += char.lower()

        if len(new) % 2 == 0:
            half = len(new) // 2
            first_half = new[0:half]
            second_half = new[half:]
            return first_half == second_half[::-1]
        else:
            half = len(new) // 2
            first_half = new[0:half]
            second_half = new[half+1:len(new)+1]
            return first_half == second_half[::-1]
