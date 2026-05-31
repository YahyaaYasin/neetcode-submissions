class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        out = []
        for i in range(len(nums)):
            first = nums[i]
            second = target - first
            if second in hashmap:
                out.append(nums.index(second))
                out.append(i)
            else:
                hashmap[first] = second
        return out
            
        