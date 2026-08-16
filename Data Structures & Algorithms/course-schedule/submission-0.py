class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create Adjustancy List using Hashmap
        preMap = {i:[] for i in range(numCourses)}
        # Create list with crs,pre
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        #Visit set in order to track the cycle
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        