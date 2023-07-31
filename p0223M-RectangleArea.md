> Problem: [223. 矩形面积](https://leetcode.cn/problems/rectangle-area/description/)

# 思路
> 这道题都没做出来，，被我自己蠢死，，，，，

# 复杂度
- 时间复杂度:  $O(1)$

# Code
```Python []

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        s1 = (ax2 - ax1)*(ay2 - ay1)
        s2 = (bx2 - bx1)*(by2 - by1)
        overlapwidth = min(ax2,bx2) - max(ax1,bx1)
        overheight = min(ay2,by2) - max(ay1,by1)
        overlapS = max(overlapwidth,0) * max(overheight,0)
        return s1 +s2 - overlapS

```
