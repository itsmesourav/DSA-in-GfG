class Solution:
    def canSeatAllPeople(self, k, seats):
        n = len(seats)

        # Check if current arrangement is already invalid
        for i in range(n - 1):
            if seats[i] == 1 and seats[i + 1] == 1:
                return False

        # If no new people need to be seated
        if k == 0:
            return True

        # Greedily place people
        for i in range(n):
            if seats[i] == 0:
                left = (i == 0 or seats[i - 1] == 0)
                right = (i == n - 1 or seats[i + 1] == 0)

                if left and right:
                    seats[i] = 1
                    k -= 1

                    if k == 0:
                        return True

        return False