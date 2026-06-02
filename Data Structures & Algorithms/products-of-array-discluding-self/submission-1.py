class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        og = nums.copy()
        
        for i in range(len(nums)):

            tl = og.copy()
            tl.pop(i)

            new_num = 1

            for number in tl:
                new_num *= number
            
            nums[i] = new_num
        
        return nums
