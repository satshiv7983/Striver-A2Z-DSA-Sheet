#User function Template for python3

class Solution:
    def canReach(self, nums, N):
        # code here 
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return 1 if goal == 0 else 0
