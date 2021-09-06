class Solution:
    def plusOne(self, l: List[int]) -> List[int]:
        a = str(int(''.join([str(i) for i in l]))+1)
        a = list((a))
        for j in range(0,len(a)):
            a[j] = int(a[j])
        return a

s = Solution()
s.plusOne([1,2,3,4])