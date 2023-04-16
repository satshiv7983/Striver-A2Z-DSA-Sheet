#User function Template for python3

class Solution:
    def substrCount (self,str1, k):
        def most_k_chars(s, k):
            if not s:
                return 0
            char_count = {}
            num = 0
            left = 0
         
            for i in range(len(s)):
                char_count[s[i]] = char_count.get(s[i], 0) + 1
                while len(char_count) > k:
                    char_count[s[left]] -= 1
                    if char_count[s[left]] == 0:
                        char_count.pop(s[left])
                    left += 1
                num += i - left + 1
            return num
         
        return most_k_chars(s, k) - most_k_chars(s, k - 1)
         
