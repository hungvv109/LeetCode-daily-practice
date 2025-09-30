class Solution:
    def check_Palindromic(self, s):
        start = 0
        end = len(s)-1
        check = len(s) // 2
        while start < check:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        size_window = len_s
        while size_window > 0:
            for i in range(len_s - size_window + 1):
                if self.check_Palindromic(s[i:i+size_window]):
                    return s[i:i+size_window]
            size_window -= 1
        return s[0]