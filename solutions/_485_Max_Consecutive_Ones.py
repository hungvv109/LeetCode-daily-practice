def findMaxConsecutiveOnes(nums):
	res = 0
	count = 0

	for i in nums:
		if i == 0:
			res = max(count, res)
			count = 0
		else:
			count += 1

	return max(count, res)