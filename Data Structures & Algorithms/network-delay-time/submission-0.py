class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        # Creating adjustancy list from all the starting nodes
        for s,e,w in times:
            edges[s].append((e,w))
        
        visit = set()
        minHeap = [(0,k)]
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            
            visit.add(n1)
            t = max(t,w1)

            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w1+w2,n2)) # we will push prevWeight + currentWright in MinHeap
        
        return t if len(visit) == n else -1

        

        