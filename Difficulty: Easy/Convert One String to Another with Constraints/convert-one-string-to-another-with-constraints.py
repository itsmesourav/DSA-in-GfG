class Solution:
    def isItPossible(self, s1: str, s2: str) -> bool:
        # Step 1: If lengths are different, they can't match
        if len(s1) != len(s2):
            return False

        # Step 2: Check if the sequence of non-'#' characters is the same
        filtered_s1 = [c for c in s1 if c != '#']
        filtered_s2 = [c for c in s2 if c != '#']

        if filtered_s1 != filtered_s2:
            return False

        # Step 3: Check indices for 'A' and 'B' movements
        # 'A' can only move left (s1 index >= s2 index)
        # 'B' can only move right (s1 index <= s2 index)
        i, j = 0, 0
        n = len(s1)

        while i < n and j < n:
            # Find the next non-'#' character in s1
            while i < n and s1[i] == '#':
                i += 1
            # Find the next non-'#' character in s2
            while j < n and s2[j] == '#':
                j += 1

            if i < n and j < n:
                # The characters must match (we already checked filtered equality, but good to ensure)
                if s1[i] != s2[j]:
                    return False

                # Check movement constraints
                if s1[i] == 'A' and i < j:
                    return False  # 'A' cannot move right
                if s1[i] == 'B' and i > j:
                    return False  # 'B' cannot move left

                i += 1
                j += 1

        return True