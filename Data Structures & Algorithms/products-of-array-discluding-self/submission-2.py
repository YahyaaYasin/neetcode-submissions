class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        zeroCount = 0

        for num in nums:
            if num == 0:
                zeroCount += 1
                continue
            else:
                product *= num
        
        if zeroCount > 1:
            return [0] * len(nums)

        elif zeroCount == 1:
            indexOfZero = nums.index(0)
            lst = [0] * len(nums)
            lst[indexOfZero] = product
            return lst
        
        else:
            for i in range(len(nums)):
                productExceptSelf = int(product/nums[i])
                nums[i] = productExceptSelf

        return nums
        