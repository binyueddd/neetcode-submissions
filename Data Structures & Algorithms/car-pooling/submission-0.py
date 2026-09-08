class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_location = max(dest for _,_, dest in trips)
        passengers = 0

        for location in range(max_location+1):
            for num, start, end in trips:
                if end==location:
                    passengers-=num
                if start == location:
                    passengers+=num
                
            if passengers > capacity:
                return False
    
        return True

            