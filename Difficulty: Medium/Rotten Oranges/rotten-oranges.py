class Solution:
	def orangesRot(self, mat):
	    rows, cols = len(mat), len(mat[0])
	    queue = deque()
	    fresh = 0
	    
	    for r in range(rows):
	        for c in range(cols):
	            if mat[r][c] == 2:
	                queue.append((r, c))
	            elif mat[r][c] == 1:
	                fresh += 1
	                
	    if fresh == 0:
	        return 0
	        
	    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	    time = 0
	       
	    while queue:
	        size = len(queue)
	        infected = False
	           
	        for _ in range(size):
	            r, c = queue.popleft()
	               
	            for dr, dc in directions:
	                nr, nc = r + dr, c + dc
	                   
	                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == 1:
	                    mat[nr][nc] = 2
	                    queue.append((nr, nc))
	                    fresh -= 1
	                    infected = True
	           
	        if infected:
	            time += 1
	               
        return time if fresh == 0 else -1
		