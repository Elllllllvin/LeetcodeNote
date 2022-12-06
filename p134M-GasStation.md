> Problem: [134. 加油站](https://leetcode.cn/problems/gas-station/description/)

# 思路

## 1.暴力法（Code2）：

自己想的蠢办法：能过但是击败 5.5%💧

## 2.别人的方法：

剪枝:如果从 x 经过 z 到 y 后`totalGas<totalCost`,说明 x 无法到达 y+1 点，x 经过 z 说明 x 能到 z，那么可以得出 z 不能到 y，因此，对于 x 到 y，若 x 不能到 y+1，那么 x 与 y 中间的所有点均不可能到达 y+1，所以直接把 start 换到 y+1 重新开始即可。

# Code1 又是别人写的神仙解法呀~

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

```Python []

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = 0
        totalCost = 0
        totalGas  = 0
        tempGas = 0
        for i in range(n):
            totalGas += gas[i]
            totalCost += cost[i]
            tempGas += gas[i]-cost[i]
            if tempGas<0:
                start = i+1
                tempGas = 0

        if totalCost>totalGas:
            return -1
        else:
            return start
```

# Code2 暴力法：蠢但是过了，虽然时间非常非常长

- 时间复杂度: $O(n^2)$
- 空间复杂度: $O(1)$

```Python []

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = -1
        for i in range(n-1,-1,-1):
            totalGas = 0
            flag = 1
            if gas[i] == 0:
                continue
            for j in range(n):
                totalGas = totalGas+gas[(i+j)%n] - cost[(i+j)%n]
                if totalGas < 0:
                    flag = 0
                    break

            if flag:
                start = i
                break
        return start
```
