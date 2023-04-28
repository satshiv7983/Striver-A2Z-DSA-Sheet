#User function Template for python3

class Solution:
    def countSubarray(self, n, nums, k):
        
        dic = { 0: 1 }
		cnt = res = 0
		for idx, num in enumerate(nums):
			if num % 2 == 1:
				cnt += 1

			if cnt - k in dic:
				res += dic[cnt-k]

			dic[cnt] = dic.get(cnt, 0) + 1

		return res 
