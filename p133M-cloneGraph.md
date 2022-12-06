> Problem: [133. 克隆图](https://leetcode.cn/problems/clone-graph/description/)

# 思路

> dfs 构图

# Code

```Python []

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        vis = {}
        def dfs(node):
            if node == None:
                return
            if node in vis:
                return vis[node]
            new_node =  Node()
            new_node.val = node.val
            vis[node] = new_node

            for item in node.neighbors:
                new_node.neighbors.append(dfs(item))

            return new_node

        return dfs(node)


```
