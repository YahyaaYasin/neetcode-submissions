class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lowest=1                    #lowest K
        highest=max(piles)          #highest K
        out = highest

        while lowest <= highest:

            mid = (lowest+highest) // 2

            # calculate how long will it take to eat
            count=0
            for i in piles:
                if i % mid == 0:
                    count += (i//mid)
                else:
                    count += (i//mid)+1

            if count <= h:
                out = min(out, mid)
                highest = mid - 1
            else:
                lowest = mid + 1
        
        return out






        
        