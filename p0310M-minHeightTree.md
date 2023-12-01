> Problem: [310. 最小高度树](https://leetcode.cn/problems/minimum-height-trees/description/)

[TOC]

# 思路
> BFS的变种题，好难！！细细体会

# 解题方法
> 描述你的解题方法

# 复杂度
- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

# Code
```Python []

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        if n == 1:
            return [0]
        
        degree = [0]*n
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1
        
        queue = deque()
        for i in range(len(degree)):
            if degree[i] == 1:
                queue.append(i)
                degree[i] -= 1
        
        while queue:
            res = []
            for _ in range(len(queue)):
            # 每次遍历degree为1的式子，升到最后的一定是最小高度树，因此最长路径的中点作为根就是最小高度树
                i = queue.popleft()
                res.append(i)
                # 一层一层把叶子结点剥掉
                # 最后一轮剩下的结果就是答案
                for neighbor in adj[i]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)

        return res




            
        



```
