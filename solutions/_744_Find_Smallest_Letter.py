class Solution:
    def nextGreatestLetter(self, letters, target) -> str:
        if letters[len(letters)-1] <= target or letters[0] > target:
            return letters[0]

        a = 0
        b = len(letters)-1

        while a < b:
            mid = (a + b) // 2
            if letters[mid]  <= target:
                a = mid+1
            else:
                b = mid

        return letters[a]
        