class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create adjustancy lisst
        preMap = {crs:[] for crs in range(numCourses)}

        #Create list with crs and it's prerequisites
        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        res = []        
        visit = set() # set to add already visited course
        cycle = set() # Set to detect cycle
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res
        
        # print(res,res2)
        return list(res) if res else []