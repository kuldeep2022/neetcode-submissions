class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)

        # Create adj list
        for src,dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        
        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
           
            res.append(src)
        dfs('JFK')
        
        # print(res[::-1])
        return res[::-1]
        