class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        b = []

        for i in range(n):
            while nums[i] == 0:
                b.append(0)
                nums.pop(i)

        nums += b