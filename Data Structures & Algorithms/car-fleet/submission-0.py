class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]

        for pos, v in zip(position, speed):
            time = (target-pos)/v
            cars.append((pos,time))
        
        cars.sort(reverse=True)
        
        cur_time=0
        fleets=0

        for p, time in cars:
            if time > cur_time:
                cur_time=time
                fleets+=1
        
        return fleets