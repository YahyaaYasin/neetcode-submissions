class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        out = []

        for num in nums:

            ls = 1

            next_number = True
            number = num

            while next_number:

                if number + 1 in nums:
                    ls += 1
                    number += 1
                else:
                    next_number = False

            out.append(ls)
        
        if out == []:
            return 0
        else:
            return max(out)

            
        