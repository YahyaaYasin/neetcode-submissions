class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1

        while l < r:

            mid = (l + r) // 2
            
            # at the point of deflection, nums[i] > nums[i+1] so
            if nums[mid] < nums[r] :
                r = mid
            else:
                l = mid + 1

        # our point of deflection is l-1, so seperate both sorted lists
        split = l

        #decide which side should we search and assign left and right
        if nums[split] <= target <= nums[len(nums)-1]:
            l, r = split, len(nums)-1
        else:
            l, r = 0, split-1
            

        # another binary search
        while l <= r:

            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return -1

        