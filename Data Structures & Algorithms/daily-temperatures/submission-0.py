class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res=[0]*len(temperatures)
        stack = [] # pair (temp, index)

        for index, item in enumerate(temperatures):

            while stack and item > stack[-1][0]:

                stackTemp,stackIndx=stack.pop()
                res[stackIndx] = index-stackIndx

            stack.append((item,index))

        return res
            
            


        