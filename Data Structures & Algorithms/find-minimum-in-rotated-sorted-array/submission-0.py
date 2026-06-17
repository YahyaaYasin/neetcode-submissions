class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        sorted_num = sorted(nums)
        return sorted_num[0]

        # # Base case
        # if nums == [] 
        #     return 0
        # elif nums == sorted_num:
        #     return sorted_num[0]

        # min = 
        # while True:

        #     last_num = sorted_num.pop()
        #     sorted_num.insert(0, last_num)

        #     min_rotation += 1

        #     if sorted_num == nums:
        #         return min_rotation
        #     else:
        #         continue

