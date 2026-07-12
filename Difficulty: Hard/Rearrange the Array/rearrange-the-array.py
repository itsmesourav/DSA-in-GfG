class Solution:
    def minOperations(self, b):
        MOD = 10**9 + 7
        n = len(b)

        # Sieve for smallest prime factor
        spf = list(range(n + 1))
        for i in range(2, int(n**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, n + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        visited = [False] * n
        prime_exp = {}

        for i in range(n):
            if not visited[i]:
                cur = i
                length = 0
                while not visited[cur]:
                    visited[cur] = True
                    cur = b[cur] - 1
                    length += 1

                x = length
                while x > 1:
                    p = spf[x]
                    cnt = 0
                    while x % p == 0:
                        x //= p
                        cnt += 1
                    prime_exp[p] = max(prime_exp.get(p, 0), cnt)

        ans = 1
        for p, e in prime_exp.items():
            ans = (ans * pow(p, e, MOD)) % MOD

        return ans