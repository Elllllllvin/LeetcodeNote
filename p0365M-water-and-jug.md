> Problem: [365. 水壶问题](https://leetcode.cn/problems/water-and-jug-problem/description/)

[toc]

# 思路

> 法一：dfs （dfs导致的递归远远超过的python的默认递归层数，因此这里用栈来模拟递归）
> 法二：数学方法。经推导得出，每次操作只会让桶里的水总量增加 x，增加 y，减少 x，或者减少 y

# 解题方法

> 法一：dfs，一种一种的试，时间很慢
> 法二：因此我们的目标可以改写成：找到一对整数 a,b，使得 ax+by=z，贝祖定理告诉我们，ax+by=z 有解当且仅当 z是 x,y 的最大公约数的倍数。因此我们只需要找到 x,y的最大公约数并判断 z 是否是它的倍数即可。
作者：力扣官方题解
链接：https://leetcode.cn/problems/water-and-jug-problem/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 复杂度
法一：
- 时间复杂度: $O(jug1Capacity*jug2Capacity)$
- 空间复杂度: $O(jug1Capacity*jug2Capacity)$

# Code1

```Python
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        stack = [(0,0)]
        tmpset = set()
        while stack:
            remain_1 , remain_2 = stack.pop()
            if remain_1 == targetCapacity or remain_2 == targetCapacity or remain_1 + remain_2 == targetCapacity:
                return True
            if (remain_1,remain_2) in tmpset:
                continue
            tmpset.add((remain_1,remain_2))
            # 倒空x
            stack.append((0,remain_2))
            # 倒空y
            stack.append((remain_1,0))
            # 倒满x
            stack.append((jug1Capacity,remain_2))
            # 倒满y
            stack.append((remain_1,jug2Capacity))
            # x倒入y
            stack.append((remain_1 - min(jug2Capacity-remain_2,remain_1),remain_2 + min(jug2Capacity-remain_2,remain_1)))
            # y倒入x
            stack.append((remain_1+min(jug1Capacity-remain_1,remain_2),remain_2-min(jug1Capacity-remain_1,remain_2)))
        return False
```

# Code2
```Python []

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        if jug1Capacity==0 or jug2Capacity == 0:
            return targetCapacity == 0 or jug1Capacity+jug2Capacity==0

        return targetCapacity % math.gcd(jug1Capacity,jug2Capacity) == 0
```
  
