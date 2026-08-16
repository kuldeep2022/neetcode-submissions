class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n or not edges: return True

        preMap = {i:[] for i in range(n)}

        for s,e in edges:
            preMap[s].append(e)
            preMap[e].append(s)
        
        visit = set()
        def dfs(node,prev):
            if node in visit:
                return False
            if preMap[node] == []:
                return True
            
            visit.add(node)

            for nei in preMap[node]:
                if nei == prev:
                    continue
                if not dfs(nei,node): return False
            
            return True
        return dfs(0,-1) and n == len(visit)
            
        