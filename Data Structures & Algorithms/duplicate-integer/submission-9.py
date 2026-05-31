class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty = []
        for i in nums:
            if i in empty:
                return True
            else:
                empty.append(i)
        return False
