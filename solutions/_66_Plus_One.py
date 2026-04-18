class Solution:
	def plusOne(self, digits):
		num = int(''.join(map(str, digits)))
		num += 1
		
		lst = []
		while num != 0:
			lst.append(num % 10)
			num //= 10

		return lst[::-1]