class Solution:
    def countPrimes(self, l: int) -> int:
        count = 0
        count1 = 0
        if l>2:
            for j in range(2,l):
                for i in range(1,(j+1)):
                    if j % i == 0:
                        count +=1
                if count > 2:
                    count = 0 
                    pass
                else:
                    count1+=1
                    count = 0
            return count1
        else:
            return 0

s = Solution()
s.countPrimes(10)