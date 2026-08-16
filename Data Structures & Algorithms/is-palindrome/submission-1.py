class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for i in s:
            if i.isalnum():
                res.append(i.lower())
        
        return "".join(res) == "".join(res[::-1])

        