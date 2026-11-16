class Solution:
    def findPattern(self, s):
        i = 0
        n = len(s)

        while i < n:
            count_x = 0
            count_y = 0

            # Count consecutive x's
            while i < n and s[i] == 'x':
                count_x += 1
                i += 1

            # Count consecutive y's
            while i < n and s[i] == 'y':
                count_y += 1
                i += 1

            # Both counts must be equal
            if count_x == 0 or count_x != count_y:
                return False

        return True