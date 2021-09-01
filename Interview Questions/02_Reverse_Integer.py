class Solution:
    def reverse(self, num: int) -> int:
        name=str(num)
        if name[0] == "-":
            num = int("-" + name[:0:-1])
            if pow(-2,31)<=num<=(pow(2,31)-1):
                return num
            else:
                return 0 
        else:
            num = int(name[::-1])
            if pow(-2,31)<=num<=(pow(2,31)-1):
                return num
            else:
                return 0
        

s = Solution()
s.reverse(-123)