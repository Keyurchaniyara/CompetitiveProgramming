class Solution:
    def firstUniqChar(self, c: str) -> int:
        s1=set(c)
        for i in range(len(c)):
            if c.count(c[i])==1:
                return c.index(c[i])
                break
        if len(s1)<=len(c):
            return -1
        

s = Solution()
s.firstUniqChar("Hello Hi")