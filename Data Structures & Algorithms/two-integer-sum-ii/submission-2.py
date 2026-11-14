class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #sorted array in increasing order
        # [1,2,3,4]     target=3
        # use two pointer from both end
        # current value (addition of the left and right pointer) > target, right pointer-1
        # current value (addition of the left and right pointer) < target, left pointer-1

        leftPointer,rightPointer=0,len(numbers)-1

        while leftPointer < rightPointer:
            currentValue=numbers[leftPointer]+numbers[rightPointer]

            if currentValue > target:
                rightPointer-=1   

            elif currentValue < target:
                leftPointer+=1
            
            else:
                return [leftPointer+1, rightPointer+1]

        