#User function Template for python3

class Solution:
    def pageFaults(self, n, c, pages):
        count = 0
 
    # To store elements in memory of size c
        v = []
     
        # Iterate through all elements of pages
        for i in range(n):
     
            # Find if element is present in memory or not
            if pages[i] not in v:
     
                # If memory is full
                if len(v) == c:
     
                    # Remove the first element
                    # As it is least recently used
                    v.pop(0)
     
                # Add the recent element into memory
                v.append(pages[i])
     
                # Increment the count
                count += 1
            else:
     
                # If element is present
                # Remove the element
                # And add it at the end as it is
                # the most recent element
                v.remove(pages[i])
                v.append(pages[i])
     
        # Return total page faults
        return count
