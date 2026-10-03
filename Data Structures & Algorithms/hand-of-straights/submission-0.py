class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            
            return False

        counter={}
        for a in hand:
            counter[a] = 1+ counter.get(a, 0)

        minH = list(counter.keys())
        heapq.heapify(minH)

        while minH:
            top = minH[0]

            for i in range(top, top+groupSize):
                if i not in counter:
                    print("a")
                    return False
                counter[i]-=1
                if counter[i]==0:
                    if i != minH[0]:
                        print("b")
                        return False
                    heapq.heappop(minH)
        return True