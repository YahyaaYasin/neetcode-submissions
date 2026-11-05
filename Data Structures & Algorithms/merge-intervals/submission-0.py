class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 1:
            return intervals
        
        out = []

        intervals.sort(key=lambda x : x[0])

        i = 0
        lengthOfRemaining = len(intervals)

        while i < lengthOfRemaining:
            
            if i+1 > len(intervals)-1:
                return intervals

            #merge possible
            if intervals[i][1] >= intervals[i+1][0]:
                
                newStart = intervals[i][0]
                newEnd = max(intervals[i][1], intervals[i+1][1])
                intervals[i+1][0] = newStart
                intervals[i+1][1] = newEnd

                intervals.pop(i)
            
            #merge not possible
            else: 
                i += 1

        return intervals


            

            
        
            
        