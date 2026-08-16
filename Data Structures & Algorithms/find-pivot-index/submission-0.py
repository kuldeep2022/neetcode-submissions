class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        pre = 0
        for n in nums:
            pre += n
            prefix.append(pre)
        
        pv = 0
        for l in range(len(prefix)):
            if l == 0:
                if pv == (prefix[-1] - prefix[l]):
                    return l
            else:
                if prefix[l-1] == prefix[-1] - prefix[l]:
                    return l
        
        return -1
                
            