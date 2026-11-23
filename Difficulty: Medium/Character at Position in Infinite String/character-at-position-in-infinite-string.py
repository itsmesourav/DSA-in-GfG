
class Solution:
    def posInfinite(self, s: str, pos: int) -> str:

        n = len(s)
        lengths = [n]

        i = 1

        # Calculate lengths until pos is covered
        while lengths[-1] < pos:
            lengths.append(2 * lengths[-1] + i)
            i += 1

        # Find the character by moving backwards
        for i in range(len(lengths) - 1, 0, -1):

            prev = lengths[i - 1]
            mid = i

            if pos <= prev:
                continue

            elif pos <= prev + mid:
                return '$'

            else:
                pos = 2 * prev + mid - pos + 1

        return s[pos - 1]
