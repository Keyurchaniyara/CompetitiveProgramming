class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            if 1<=len(s)<=(5*pow(10,4)): 
                return True
        else:
            if 1<=len(s)<=(5*pow(10,4)):
                return False
        
        
        

s = Solution()
s.isAnagram("anagram","nagaram")