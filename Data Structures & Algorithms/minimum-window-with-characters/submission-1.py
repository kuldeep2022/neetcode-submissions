class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        window, countT = {},{}
        for value in t:
            countT[value] = countT.get(value,0) + 1

        res, resLen = [-1,-1], float('inf')
        have, need = 0, len(countT)
        l = 0

        for r,v in enumerate(s):
            window[v] = window.get(v,0) + 1
            if v in countT and window[v] == countT[v]:
                have += 1
            
            while have == need:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    res = [l,r]
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1
        
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""



                
        