> Problem: [87. 扰乱字符串](https://leetcode.cn/problems/scramble-string/description/)

# 思路

> 记忆化递归
> 在 Python 中，有一个实现记忆化递归的神器，就是 `functool`模块的 `lru_cache`装饰器，它可以把函数的输入和输出结果缓存住，在后续调用中如果遇到了相同的输入，直接从缓存里面读。顾名思义，它使用的是 LRU （最近最少使用）的缓存淘汰策略。**或者可以直接写**`@cache`

# 解题方法

# Code1 记忆化递归

```Python []
class Solution:
    # @functools.lru_cache(None)
    @cache #可以直接写@cache
    def isScramble(self, s1: str, s2: str) -> bool:
        N = len(s1)
        if N == 0: return True
        if N == 1: return s1 == s2
        if sorted(s1) != sorted(s2):
    # sorted( )函数是返回一个新的list,不在原来的list上进行操作，调用其返回一个排好序的list。
            return False
        for i in range(1, N):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            elif self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False

```
