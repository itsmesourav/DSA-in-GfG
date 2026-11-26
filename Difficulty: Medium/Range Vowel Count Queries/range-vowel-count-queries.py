class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:

        n = len(s)
        prefix = [0] * n
        vowels = "aeiou"

        # Build prefix sum
        for i in range(n):
            prefix[i] = (prefix[i - 1] if i > 0 else 0)

            if s[i] in vowels:
                prefix[i] += 1

        # Process queries
        ans = []

        for l, r in queries:
            if l == 0:
                ans.append(prefix[r])
            else:
                ans.append(prefix[r] - prefix[l - 1])

        return ans