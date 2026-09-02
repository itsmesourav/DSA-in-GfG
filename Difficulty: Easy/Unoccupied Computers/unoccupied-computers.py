class Solution:
    def solve(self, n, s):
        occupied = 0
        ans = 0
        seen = set()
        assigned = set()

        for ch in s:
            if ch not in seen:
                # First occurrence = arrival
                seen.add(ch)

                if occupied < n:
                    occupied += 1
                    assigned.add(ch)
                else:
                    ans += 1

            else:
                # Second occurrence = departure
                if ch in assigned:
                    occupied -= 1
                    assigned.remove(ch)

        return ans