> Problem: [313. 超级丑数](https://leetcode.cn/problems/super-ugly-number/description/)

[TOC]

# 思路
> 动态规划，丑数II的拓展

# 解题方法
> 描述你的解题方法

# 复杂度
- 时间复杂度:  $O(n*len(primes))$

- 空间复杂度:  $O(n)$

# Code
```Python []

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1]*n #建立一个动态规划数组
        primes_length = len(primes)
        primes_index = [0]*primes_length
        # 这个primes_index 和 primes 是一一对应的，表示primes[j]该乘以dp中的哪一个了
        for i in range(1,n):
            candidate = [0]*primes_length
            # 记录primes[j]*dp[primes_index[j]]组成的整个数组，这个数组中存放着成为dp[i]元素的候选
            # 最后candidate数组中的最小值当选
            cur_min = inf
            for j in range(primes_length):
                t = primes[j]*dp[primes_index[j]]
                candidate[j] = t
                if cur_min > t: #找到数组中的最小值
                    cur_min = t
            # 候选值可能会重复（例如2*2*3 和3*4），因此对于重复的情况，有多个primes_index要更新！！
            for j in range(primes_length):
                if candidate[j] == cur_min:
                    primes_index[j] += 1
            dp[i] = cur_min #真正的候选值！
        
        return dp[-1]



```
