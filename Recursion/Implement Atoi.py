
class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        if not string.strip('-').isnumeric():
            return -1
        if len(string)-len(string.strip('-'))>=2:
            return -1
        res = 0
        # initialize sign as positive
        sign = 1
        i = 0
    
        # if number is negative then update sign
        if string[0] == '-':
            sign = -1
            i += 1
    
        # Iterate through all characters 
        # of input string and update result
        for j in range(i, len(string)):
            res = res*10+(ord(string[j])-ord('0'))
    
        return sign * res
    
   # recursive solution

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        if not string.strip('-').isnumeric():
                return -1
        if len(string)-len(string.strip('-'))>=2:
            return -1
        def recur(string,num):
            if string.isalpha():
                return -1
            
            if len(string)==1:
                return int(string)+num*10
            
            num=int(string[:1])+num*10
            
            return recur(string[1:],num)
        if string[0]=='-':
            return -1*recur(string[1:],0)
        return recur(string,0)
                

