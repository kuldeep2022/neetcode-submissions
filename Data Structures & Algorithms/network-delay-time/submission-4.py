class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)

        for src,dst,w in times:
            adj[src].append((w,dst)) #(wieght, dst)
        
        minHeap = [(0,k)]
        visit = set()
        ans = 0
        while minHeap:
            w,node = heapq.heappop(minHeap)

            if node in visit:
                continue
            visit.add(node)
            ans = w

            for weight, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap,(w+weight, nei))
        
        return ans if len(visit) == n else -1

