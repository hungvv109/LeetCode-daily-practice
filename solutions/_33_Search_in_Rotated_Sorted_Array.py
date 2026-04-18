class Solution:
    def divide(self, nums, a, b, target):
        if a == b:
            return a if nums[a] == target else -1

        mid = (a + b) // 2

        if nums[mid] == target:
            return mid
        
        nums1 = self.divide(nums, a, mid, target)
        nums2 = self.divide(nums, mid+1, b, target)

        if nums1 != -1:
            return nums1
        return nums2

    def search(self, nums, target) -> int:
        n = len(nums)
        
        if n == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        idx = self.divide(nums, 0, n-1, target)

        return idx

nums = [4,5,6,7,0,1,2]
target = 0
t = Solution().search(nums, target)
print(t)