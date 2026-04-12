class Solution:
    def nextPalindrome(self, num):
        n = len(num)
        
        # 🔥 EDGE CASE: all 9s
        if all(x == 9 for x in num):
            return [1] + [0] * (n - 1) + [1]
        
        # Step 1: mirror left → right
        pal = num[:]
        i, j = 0, n - 1
        
        while i < j:
            pal[j] = pal[i]
            i += 1
            j -= 1
        
        # Step 2: if already greater, return
        if pal > num:
            return pal
        
        # Step 3: increment middle
        carry = 1
        mid = n // 2
        
        if n % 2 == 1:
            pal[mid] += carry
            carry = pal[mid] // 10
            pal[mid] %= 10
            left = mid - 1
            right = mid + 1
        else:
            left = mid - 1
            right = mid
        
        # propagate carry
        while left >= 0:
            pal[left] += carry
            carry = pal[left] // 10
            pal[left] %= 10
            pal[right] = pal[left]
            left -= 1
            right += 1
        
        return pal