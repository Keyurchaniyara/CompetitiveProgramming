class Solution:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        arr.sort()
        result = ""
        for i in range(len(arr[0])):
            if arr[0][i] == arr[-1][i]:
                result += arr[0][i]
            else:
                break
        return result

arr = ["flower","flow","flight"]    
s = Solution()
s.longestCommonPrefix(arr)