"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        copy=Node(node.val)
        cloned={}
        
        cloned[node]=copy
        queue=deque([node])

        while queue:
            cur=queue.popleft()

            for nbr in cur.neighbors:
                if nbr not in cloned:
                    
                    cloned[nbr]=Node(nbr.val)
                    queue.append(nbr) # append neighbor 前，必须保证 cloned[nbr] 已经存在
                cloned[cur].neighbors.append(cloned[nbr])
        
        return copy
                

