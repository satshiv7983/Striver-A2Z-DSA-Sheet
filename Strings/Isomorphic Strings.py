class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        n,m=len(str1),len(str2)
        if n!=m:
            return 0
        hashmap={}
        for i in range(n):
            if str1[i] in hashmap:
                if hashmap[str1[i]]!=str2[i]:
                    return 0
                    
            else:
                hashmap[str1[i]]=str2[i]
        if len(set(hashmap.values()))!=len(hashmap.values()):
            return 0
        return 1
