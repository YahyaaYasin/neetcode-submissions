class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #base
        if nums == []:
            return 0

        numSet = set(nums)
        longest = 0

        for num in nums:
            if num-1 in numSet:
                continue
            else:
                length = 1
                while (num+1) in numSet:
                    length += 1
                    num += 1
                
                longest = max(length, longest)

        return longest
        