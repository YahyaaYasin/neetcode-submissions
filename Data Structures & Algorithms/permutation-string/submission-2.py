class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        windowSize=len(s1)
        s1=sorted(s1)

        for i in range(len(s2)-windowSize+1):

            window = s2[i:i+windowSize]

            if sorted(window) == s1:
                return True

        return False        

        # this is a O(n · m log m) solution. n=len(s2) & m=len(s1)
        # optimal solution would be to use "counter" instead of "sorted" bringing the solution to O(n·m)