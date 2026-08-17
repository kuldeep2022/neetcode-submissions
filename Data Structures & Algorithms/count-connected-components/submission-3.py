class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.components = n
    
    def find(self,n):
        if n != self.par[n]:
            return self.find(self.par[n])
        else:
            return n
    
    def union(self,n1,n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]

        self.components -= 1
        return True



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        
        for n1,n2 in edges:
            uf.union(n1,n2)
        
        return uf.components

        'I am trying to solve this using DFS'
        adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = [False] * n

        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        
        return res

        