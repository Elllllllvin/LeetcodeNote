_Italic_> Problem: [207. 课程表 II](https://leetcode.cn/problems/course-schedule/description/)

# 思路

使用 dfs 方法，代码稍微与 1 不太一样

## 方法 1：dfs 深度优先搜索

使用一个栈来存储已经搜索完成的节点。

- 对于某个节点 u，如果它的所有相邻节点都已经搜索完成，那么在搜索回溯到 u 的时候，u 本身也会变成一个已经搜索完成的节点。这里的「相邻节点」指的是从 u 出发通过一条有向边可以到达的所有节点。

算法：将任意节点标记为三种状态：未搜索，搜索中，已搜索
通过上述的三种状态，我们就可以给出使用深度优先搜索得到拓扑排序的算法流程，在每一轮的搜索搜索开始时，我们任取一个「未搜索」的节点开始进行深度优先搜索。

我们将当前搜索的节点 u 标记为「搜索中」，遍历该节点的每一个相邻节点 v：

- 如果 v 为「未搜索」，那么我们开始搜索 v，待搜索完成回溯到 u；
- **如果 v 为「搜索中」，那么我们就找到了图中的一个环，因此是不存在拓扑排序的**；
- 如果 v 为「已完成」，那么说明 v 已经在栈中了，而 u 还不在栈中，因此 u 无论何时入栈都不会影响到 (u,v) 之前的拓扑关系，以及不用进行任何操作。
- 当 u 的所有相邻节点都为「已完成」时，我们将 u 放入栈中，并将其标记为「已完成」。

在整个深度优先搜索的过程结束后，如果我们没有找到图中的环，那么栈中存储这所有的 n 个节点，从栈顶到栈底的顺序即为一种拓扑排序。

## Code1 dfs

时间复杂度：o(m + n)
空间复杂度：o(m + n)

```Python []
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(list)
        valid = True
        visited = [0]*numCourses
        res = []

        for info in prerequisites:
            edges[info[0]].append(info[1])

        def dfs(u):
            nonlocal valid
            if not valid:
                return

            if visited[u] == 0:
                visited[u] = 1
                for v in edges[u]:
                    dfs(v)
                visited[u] = 2
                res.append(u)
            elif visited[u] == 1:
                valid = False



        for i in range(numCourses):
            if valid and visited[i]== 0:
                dfs(i)

        return res if valid else []
```
