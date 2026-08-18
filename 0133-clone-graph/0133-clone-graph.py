"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        my_dict = {}
        qu = deque()
        qu.append(node)
        visited = set()

        while qu:
            original_node = qu.pop()
            cloned_node = None
            if original_node in my_dict :
                cloned_node = my_dict[original_node]
            else:
                cloned_node = Node()
                cloned_node.val = original_node.val
                my_dict[original_node] = cloned_node
            
            # so till now we have fetched the cloned node from the dictionary
            # now lets iterate on the neighbours of the original node 

            for child in original_node.neighbors:
                if child not in my_dict:
                    cloned_child = Node()
                    cloned_child.val = child.val
                    my_dict[child] = cloned_child
                    qu.append(child)
                my_dict[original_node].neighbors.append(my_dict[child])
        return my_dict[node]
