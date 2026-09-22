class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        pos = [[] for _ in range(26)]

        for i, ch in enumerate(s):
            pos[ord(ch) - ord('a')].append(i)

        def check(word):
            prev = -1

            for ch in word:
                arr = pos[ord(ch) - ord('a')]

                left, right = 0, len(arr)

                while left < right:
                    mid = (left + right) // 2

                    if arr[mid] > prev:
                        right = mid
                    else:
                        left = mid + 1

                if left == len(arr):
                    return False

                prev = arr[left]

            return True

        ans = ""

        for word in d:
            if check(word):
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word

        return ans