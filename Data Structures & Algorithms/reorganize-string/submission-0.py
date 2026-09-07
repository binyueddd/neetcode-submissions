class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(heap)

        res = []

        while len(heap)>1:
            freq1, ch1 = heapq.heappop(heap)
            freq2, ch2 = heapq.heappop(heap)

            res.append(ch1)
            res.append(ch2)

            freq1+=1
            freq2+=1

            if freq1<0:
                heapq.heappush(heap,(freq1, ch1))
            if freq2<0:
                heapq.heappush(heap,(freq2, ch2))

            
        if heap:
            freq, ch = heapq.heappop(heap)
            if -freq > 1:
                return ""
            
            res.append(ch)
        return "".join(res)

