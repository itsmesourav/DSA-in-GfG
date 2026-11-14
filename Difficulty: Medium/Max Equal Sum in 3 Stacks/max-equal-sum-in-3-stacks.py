
class Solution:
    def maxEqualSum(self, s1: list[int], s2: list[int], s3: list[int]) -> int:

        sum1 = sum(s1)
        sum2 = sum(s2)
        sum3 = sum(s3)

        i = j = k = 0

        while True:

            # If all three sums are equal
            if sum1 == sum2 == sum3:
                return sum1

            # Remove elements from the stack with maximum sum
            if sum1 >= sum2 and sum1 >= sum3:
                sum1 -= s1[i]
                i += 1

            elif sum2 >= sum1 and sum2 >= sum3:
                sum2 -= s2[j]
                j += 1

            else:
                sum3 -= s3[k]
                k += 1

            # If any stack becomes empty
            if i == len(s1) or j == len(s2) or k == len(s3):
                return 0
