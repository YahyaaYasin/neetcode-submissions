class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # pointer to both end
        l = 0
        r = len(nums) - 1

        # classic pointer style loop
        while l < r:

            # split in half for O(logn)
            mid = (l+r) // 2
            
            # choose the side where the min lives
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]

