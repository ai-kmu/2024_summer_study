# hash신경 안쓰고 푼 버전 업데이트 예정

class Solution(object):

	def lengthOfLongestSubstring(self, s):
	
	"""
	
	:type s: str
	
	:rtype: int
	
	"""
		# init
		data = []
		maxLen = 0
		# ===
		for i in s:
			if i in data:
			
				maxLen = maxLen if maxLen > len(data) else len(data)
				
				idx = data.index(i)
				data = data[idx+1 :]
			
			data.append(i)
		maxLen = maxLen if maxLen > len(data) else len(data)
		
		return maxLen














A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
		return maxLen
