import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # target is the distance they have to catch up
    
        fleetStack=[]

        # sort them by position in decreasing order while keeping the index in same place
        cars=sorted(zip(position, speed), reverse=True)
        
        # now add the times as fleets, 
        # if time <= to the previos one then thats a fleet otherwise new fleet

        for pos, spd in cars:

            time = (target-pos) / spd

            if not fleetStack:
                fleetStack.append(time)

            elif time > fleetStack[-1]:
                fleetStack.append(time)

        
        return len(fleetStack)
                        
        
        
        



        