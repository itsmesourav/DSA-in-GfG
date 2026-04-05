import heapq

class Node:
    def __init__(self, freq, char=None, left=None, right=None, idx=0):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.idx = idx

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.idx < other.idx
        return self.freq < other.freq


class Solution:
    def huffmanCodes(self, s, f):
        # ✅ Edge case: single character
        if len(s) == 1:
            return ["0"]
        
        heap = []
        
        # Create initial nodes
        for i in range(len(s)):
            heapq.heappush(heap, Node(f[i], s[i], idx=i))
        
        # Build Huffman Tree
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            
            new_idx = min(left.idx, right.idx)
            merged = Node(left.freq + right.freq, left=left, right=right, idx=new_idx)
            
            heapq.heappush(heap, merged)
        
        root = heap[0]
        result = []
        
        # Preorder traversal
        def dfs(node, code):
            if node.char is not None:
                result.append(code)
                return
            
            dfs(node.left, code + "0")
            dfs(node.right, code + "1")
        
        dfs(root, "")
        return result