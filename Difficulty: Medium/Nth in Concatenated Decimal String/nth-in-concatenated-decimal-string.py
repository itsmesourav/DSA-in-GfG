
class Solution:
    def nthCharacter(self, n):
        digits = 1
        count = 9
        start = 1

        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10

        number = start + (n - 1) // digits
        position = (n - 1) % digits

        return str(number)[position]
