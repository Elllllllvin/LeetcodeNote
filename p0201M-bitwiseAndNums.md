_Italic_> Problem: [201. 数字范围按位与](https://leetcode.cn/problems/bitwise-and-of-numbers-range/description/)

# 思路

位运算
暴力法时间会超时，所以采用位运算
从 left 到 right 每个数都按位与，某一位上只要有 0，那么肯定与结果为 0，从 left 增长到 right，中间每次都+1，都是不同的数，因此每次增加改变的那些位肯定全为 0，因此只需将那些改变的低位全部置为 0，再加上两个数相同的高位部分即为结果。

# Code1 右移法

```Python

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left < right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt

```

# Code2 Brian Kernighan 算法

还有一个位移相关的算法叫做「Brian Kernighan 算法」，它用于清除二进制串中最右边的 1。

Brian 算法的关键在于每次对 number 和 number-1 之间进行按位与运算后，number 中最右边的 1 会被抹去变成 0.

```Python

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            # 抹去最右边的 1
            n = n & (n - 1)
        return n

作者：力扣官方题解
链接：https://leetcode.cn/problems/bitwise-and-of-numbers-range/solutions/384938/shu-zi-fan-wei-an-wei-yu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
