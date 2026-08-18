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
        cloned_node = Node()
        cloned_node.val = node.val
        my_dict[node] = cloned_node

        qu = deque()
        qu.append(node)

        while qu:
            original_node = qu.pop()
            for child in original_node.neighbors:
                if child not in my_dict:
                    cloned_child = Node()
                    cloned_child.val = child.val
                    my_dict[child] = cloned_child
                    qu.append(child)
                my_dict[original_node].neighbors.append(my_dict[child])
        return my_dict[node]
