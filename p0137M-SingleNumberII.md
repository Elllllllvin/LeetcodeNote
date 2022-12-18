> Problem: [137. 只出现一次的数字 II](https://leetcode.cn/problems/single-number-ii/description/)

# 思路

> 位运算！！！！注意 code1，在 python 中，对 int 存储为「无符号整数类型」，而题目中是「有符号整数类型」，因此在拍段最高位时需要进行特殊处理（减去最高位的值）

# Code1 位运算

- 时间复杂度: $O(32*n)$
- 空间复杂度: $O(1)$

```Python []

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            total = sum((num >> i)&1 for num in nums)
            if total%3 == 1:
                if i == 31:
                    res -= 1 << i
                else:
                    res |= 1 << i
        return res

```

# Code2 哈希表

好方便！！：**哈希表在 python 中可以用`collections.Counter`计数来体现。该方法用于统计某序列中每个元素出现的次数，以键值对的方式存在字典中。但类型其实是 Counter。**

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

```Python []
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        ans = [num for num, occ in freq.items() if occ == 1][0]
        return ans

```
