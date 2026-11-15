class TimeMap:

    def __init__(self):
        self.book = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.book:
            self.book[key] = [(timestamp, value)]
        else:
            self.book[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.book:
            return ""

        valuesStored = self.book[key]

        left=0
        right=len(valuesStored)-1
        found = None

        while left <= right:

            mid = (left+right) // 2

            time = valuesStored[mid][0]
            val = valuesStored[mid][1]

            if time > timestamp:
                right = mid-1

            elif time <= timestamp:
                found = val
                left=mid+1

        if found:
            return found
        else:
            return ""