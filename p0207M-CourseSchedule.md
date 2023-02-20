_Italic_> Problem: [207. 课程表](https://leetcode.cn/problems/course-schedule/description/)

# 思路

拓扑排序：给定一个包含 n 个节点的有向图 G，我们给出它的节点编号的一种排列，如果满足：对于图 G 中的任意一条有向边（u，v），u 都排在 v 的前面。那么称该排列是图 G 的拓扑排序。

如果图 G 中存在环，那么就不存在拓扑排序。

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

```Python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            result.append(u)

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid
```

## 方法 2：bfs 广度优先搜索

我们使用一个队列来进行广度优先搜索。初始时，所有入度为 0 的节点都被放入队列中，它们就是可以作为拓扑排序最前面的节点，并且它们之间的相对顺序是无关紧要的。

在广度优先搜索的每一步中，我们取出队首的节点 u：

- 我们将 u 放入答案中；
- 我们移除 u 的所有出边，也就是将 u 的所有相邻节点的入度减少 1。如果某个相邻节点 v 的入度变为 0，那么我们就将 v 放入队列中。

在广度优先搜索的过程结束后。如果答案中包含了这 n 个节点，那么我们就找到了一种拓扑排序，否则说明图中存在环，也就不存在拓扑排序了。

## Code2

时间复杂度：o(m + n)
空间复杂度：o(m + n)

```Python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses


```
