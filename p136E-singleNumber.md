> Problem: [136. 只出现一次的数字](https://leetcode.cn/problems/single-number/description/)

# 思路

题目限制：必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。因此使用位运算
**若题目中说不使用额外空间，想想位运算！！**

# 解题方法

关于异或：

- 1.交换律：a ^ b ^ c <=> a ^ c ^ b
- 2.任何数于 0 异或为任何数 0 ^ n => n
- 3.相同的数异或为 0: n ^ n => 0

```Python []
a = [2,3,2,4,4]

2 ^ 3 ^ 2 ^ 4 ^ 4等价于 2 ^ 2 ^ 4 ^ 4 ^ 3 => 0 ^ 0 ^3 => 3
```

# 复杂度

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

# Code

```Python []

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n =  len(nums)
        res = 0
        for i in range(n):
            res = res^nums[i]
        return res


```
