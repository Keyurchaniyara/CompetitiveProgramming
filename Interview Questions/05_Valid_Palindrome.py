class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (''.join(filter(str.isalnum,s))).lower()
        if s == s[::-1]:
            return True
        return False

s = Solution()
s.isPalindrome("A man, a plan, a canal: Panama")