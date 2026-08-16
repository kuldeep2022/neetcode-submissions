class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adj list
        preMap = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        '''
        0: [1],
        1: []
        '''
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for cr in range(numCourses):
            if not dfs(cr):
                return False
        return True