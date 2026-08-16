class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            a = i
            count = 0
            while a>0:
                if a&1==1:
                    count+=1
                a = a >> 1
            
            res.append(count)
        
        return res