class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if matrix[-1][-1] < target:
            return False

        targetMatrix=None
        left,right=0, len(matrix)-1


        while left <= right:

            mid = (left+right) // 2

            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                targetMatrix=matrix[mid]
                break

            elif matrix[mid][-1] < target:
                left=mid+1
            
            elif matrix[mid][-1] > target:
                right=mid-1

            
        if not targetMatrix:
            return False

        left,right=0, len(targetMatrix)-1 

        while left <= right:
            mid = (left+right) // 2

            if targetMatrix[mid] < target:
                left=mid+1
            
            elif targetMatrix[mid] > target:
                right=mid-1

            elif targetMatrix[mid] == target:
                return True
            
            
        return False
