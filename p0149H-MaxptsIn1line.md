> Problem: [149. 直线上最多的点数](https://leetcode.cn/problems/max-points-on-a-line/description/)

[TOC]

# 思路

> 点斜式确定直线：遍历每一个点，根据这一个点计算其他点的斜率，即可确定该直线。

# 复杂度

- 时间复杂度: $O(n^2)$
- 空间复杂度: $O(n)$

# Code

```Python []

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n<=2:
            return n
        ans = -1
        for i in range(1,n):
            hashtbl = collections.defaultdict(int)
            for j in range(i):
                deltaX = points[j][0]-points[i][0]
                deltaY = points[j][1]-points[i][1]
                if deltaX == 0:
                    deltaY = 1
                elif deltaY == 0:
                    deltaX = 1
                if deltaX*deltaY>0:
                    deltaX = abs(deltaX)
                    deltaY = abs(deltaY)
                g = math.gcd(deltaX,deltaY)
                hashtbl[(deltaX//g,deltaY//g,)] += 1
            print(hashtbl)
            ans = max(ans,max(hashtbl.values())+1)
        return ans
```
