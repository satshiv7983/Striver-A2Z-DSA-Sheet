class Solution:
    def numberOfSubarrays(self, A, n, S):
        
        psum = {0 : 1}
        curr_sum = 0
        res = 0
        for i in A:
            # acquire
            curr_sum += i
            # check
            if curr_sum - S in psum.keys():
                res += psum.get(curr_sum - S)
            psum[curr_sum] = psum.get(curr_sum, 0) + 1
        return (res)
