class Solution:
    def commonElements(self, a, b, c):
        i, j, k = 0, 0, 0
        result = []
        last_added = None
        
        while i < len(a) and j < len(b) and k < len(c):
            
            # If all are equal → common element
            if a[i] == b[j] == c[k]:
                if a[i] != last_added:   # avoid duplicates
                    result.append(a[i])
                    last_added = a[i]
                i += 1
                j += 1
                k += 1
            
            # Move the pointer with smallest value
            elif a[i] < b[j]:
                i += 1
            elif b[j] < c[k]:
                j += 1
            else:
                k += 1
        
        return result