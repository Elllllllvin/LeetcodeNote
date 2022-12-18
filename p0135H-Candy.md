> Problem: [字节面试题！！！135. 分发糖果](https://leetcode.cn/problems/candy/description/)

# 思路

> 左遍历一遍，右遍历一遍，去最大值就是当前的最小值呀~

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$

# Code

```Python []

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        left = [1]*n
        right = [1]*n
        for i in range(n):
            if i>0 and ratings[i]>ratings[i-1]:
                left[i] = left[i-1]+1
            else:
                left[i] = 1
        for j in range(n-1,-1,-1):
            if j<n-1 and ratings[j]>ratings[j+1]:
                right[j] = right[j+1]+1
            else:
                right[j] = 1
        res = 0
        for i in range(n):
            res += max(left[i],right[i])
        return res
```
