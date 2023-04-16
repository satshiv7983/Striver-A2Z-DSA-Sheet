
class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s,goal):
        return len(s)==len(goal) and s in goal+goal
