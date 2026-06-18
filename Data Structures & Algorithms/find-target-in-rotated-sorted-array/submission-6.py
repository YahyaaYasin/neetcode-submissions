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
        ll = nums[:l]       # left list
        rl = nums[l:]       # right list 
        tl = None           # target list
        index = 0           # used to locate index of target

        #decide which side should we search
        if ll == []:
            tl = rl
            index = l
        elif ll[0] <= target <= ll[-1]:
            tl = ll
        else:
            tl = rl
            index = l

        # another binary search
        l = 0
        r = len(tl)-1

        while l <= r:

            mid = (l + r) // 2
            
            if tl[mid] == target:
                return index + mid

            elif tl[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return -1

        