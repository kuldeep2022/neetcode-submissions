class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for src,dst,w in times:
            adj[src].append((w,dst))
        
        shortest = {}
        minHeap = []
        heapq.heappush(minHeap,(0,k))
        ans = 0
        while minHeap:
            w,src = heapq.heappop(minHeap)

            if src in shortest:
                continue
            ans = max(ans,w)
            shortest[src] = w

            for wi,nei in adj[src]:
                if nei not in shortest:
                    heapq.heappush(minHeap,(wi+w,nei))
        
        print(shortest)
        return -1 if len(shortest) != n else ans


        
        

        