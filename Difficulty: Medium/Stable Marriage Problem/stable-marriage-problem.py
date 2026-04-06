class Solution:
    def stableMarriage(self, men, women):
        n = len(men)
        
        # Result arrays
        wife_of_man = [-1] * n
        husband_of_woman = [-1] * n
        
        # Track next proposal index for each man
        next_proposal = [0] * n
        
        # Precompute ranking for women
        rank = [[0] * n for _ in range(n)]
        for w in range(n):
            for i in range(n):
                rank[w][women[w][i]] = i
        
        free_men = list(range(n))
        
        while free_men:
            m = free_men.pop(0)
            
            # Get next woman to propose
            w = men[m][next_proposal[m]]
            next_proposal[m] += 1
            
            if husband_of_woman[w] == -1:
                # Woman is free
                husband_of_woman[w] = m
                wife_of_man[m] = w
            else:
                current = husband_of_woman[w]
                
                # Check preference
                if rank[w][m] < rank[w][current]:
                    # She prefers new man
                    husband_of_woman[w] = m
                    wife_of_man[m] = w
                    
                    # Previous man becomes free
                    wife_of_man[current] = -1
                    free_men.append(current)
                else:
                    # She rejects new man
                    free_men.append(m)
        
        return wife_of_man