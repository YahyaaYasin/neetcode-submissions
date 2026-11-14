class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        windowSize=len(s1)
        s1=sorted(s1)

        for i in range(len(s2)-windowSize+1):

            window = s2[i:i+windowSize]

            if sorted(window) == s1:
                return True

        return False        