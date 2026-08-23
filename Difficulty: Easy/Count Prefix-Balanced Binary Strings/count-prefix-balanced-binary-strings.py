class Solution:
    def prefixStrings(self, n: int) -> int:
        MOD = 10**9 + 7

        fact = 1
        for i in range(1, 2 * n + 1):
            fact = fact * i % MOD

        # C(2n, n) = (2n)! / (n! * n!)
        nfact = 1
        for i in range(1, n + 1):
            nfact = nfact * i % MOD

        comb = fact * pow(nfact, MOD - 2, MOD) % MOD
        comb = comb * pow(nfact, MOD - 2, MOD) % MOD

        # Catalan = C(2n,n) / (n+1)
        ans = comb * pow(n + 1, MOD - 2, MOD) % MOD

        return ans