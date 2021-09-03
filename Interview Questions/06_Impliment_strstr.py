class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if 0 <= len(haystack) and len(needle) <= (5*pow(10,4)):
            return haystack.find(needle)
        
s = Solution()
s.strStr("hello","ll")