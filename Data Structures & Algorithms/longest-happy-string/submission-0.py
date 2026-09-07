class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count = {'a': a, 'b': b, 'c': c}

        heap = [(-freq, ch) for ch, freq in count.items() if freq>0]
        heapq.heapify(heap)

        res=[]

        while heap:
            freq1, ch1 = heapq.heappop(heap)

            if len(res)>=2 and res[-1]==ch1 and res[-2]==ch1:
                if not heap:
                    break
                
                freq2, ch2 = heapq.heappop(heap)
                res.append(ch2)
                freq2+=1

                if freq2<0:
                    heapq.heappush(heap,(freq2,ch2))
                
                heapq.heappush(heap, (freq1, ch1))
            
            else:
                res.append(ch1)
                freq1+=1
                if freq1<0:
                    heapq.heappush(heap,(freq1,ch1))
                
        return "".join(res)