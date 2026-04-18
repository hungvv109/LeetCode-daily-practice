class Solution:
	def binary_search(self, nums, a, b):
		if a == b:
			return nums[a]

		mid = (a + b) // 2

		nums1 = self.binary_search(nums, a, mid)
		nums2 = self.binary_search(nums, mid+1, b)

		check = 0
		if nums1 < nums2:
			check = nums1
		else:
			check = nums2

		return check

	def findMin(self, nums):
		n = len(nums)
        
		if n == 1:
			return nums[0]

		min_num = self.binary_search(nums, 0, n-1)

		return min_num