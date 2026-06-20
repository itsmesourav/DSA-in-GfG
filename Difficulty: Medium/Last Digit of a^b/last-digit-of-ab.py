class Solution:
    def getLastDigit(self, a, b):
        # a^0 = 1 for any a (including 0 in this problem's context)
        if b == "0":
            return 1

        last = int(a[-1])

        cycles = {
            0: [0],
            1: [1],
            2: [2, 4, 8, 6],
            3: [3, 9, 7, 1],
            4: [4, 6],
            5: [5],
            6: [6],
            7: [7, 9, 3, 1],
            8: [8, 4, 2, 6],
            9: [9, 1]
        }

        cycle = cycles[last]
        length = len(cycle)

        exp_mod = 0
        for ch in b:
            exp_mod = (exp_mod * 10 + int(ch)) % length

        if exp_mod == 0:
            exp_mod = length

        return cycle[exp_mod - 1]