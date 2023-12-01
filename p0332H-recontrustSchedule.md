> Problem: [332. 重新安排行程](https://leetcode.cn/problems/reconstruct-itinerary/description/)

[toc]

# 思路

> 这道题主要是考察欧拉通路

# 解题方法

> dfs回溯

# Code1 dfs回溯 但是最后两个例子会超时

```Python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        schedule = collections.defaultdict(list)
        for ticket in tickets:
            schedule[ticket[0]].append(ticket[1])
        length = len(tickets)
        path = ['JFK']

        def dfs(cur_from):
            if len(path) == length+1:
                return True

            schedule[cur_from].sort()
            for _ in schedule[cur_from]:
                cur_to = schedule[cur_from].pop(0)
                path.append(cur_to)
                if dfs(cur_to):
                    return True
                path.pop()
                schedule[cur_from].append(cur_to)
            return False

        dfs('JFK')
        return path
```
# Code2 优化回溯
```python

class Solution:
    def findItinerary(self, tickets):

        schedule = collections.defaultdict(list)   #邻接表
        for ticket in tickets:
            schedule[ticket[0]].append(ticket[1])  # 路径存进邻接表

        for item in schedule:
            schedule[item].sort()  # 邻接表排序

        ans = []
        def dfs(cur_from):  # 深搜函数
            while schedule[cur_from]:
                dfs(schedule[cur_from].pop(0))  # 路径检索            
            ans.insert(0, cur_from)  # 放在最前

        dfs('JFK')
        return ans
```
