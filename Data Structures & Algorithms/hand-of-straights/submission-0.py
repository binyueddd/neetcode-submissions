class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        
        count=Counter(hand)

        for num in sorted(count):
            while count[num]>0:
                for x in range(num,num+groupSize):
                    if count[x]==0:
                        return False
                    count[x]-=1
        return True