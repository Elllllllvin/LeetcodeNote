> Problem: [354. 俄罗斯套娃信封问题](https://leetcode.cn/problems/russian-doll-envelopes/description/)

[TOC]

# 思路
> 法一，传统dp
> 法二，优化：基于二分查找，关键是排序的时候x从小到大，x相同时y从大到小


  
# Code1 传统dp，会超时，，
- 时间复杂度: $O(n^2)$
- 空间复杂度: $O(n)$
```Python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        sorted_envelope = sorted(envelopes, key=lambda x: (x[0], x[1]))
        # 在排序键函数 lambda x: (x[0], x[1]) 中，元组 (x[0], x[1]) 指定了两级排序。首先，它按照 x 值进行排序，然后在 x 相同时按照 y 值进行排序。
        n = len(envelopes)
        dp = [1]*n

        for i in range(1,n):
            x,y = sorted_envelope[i][0],sorted_envelope[i][1]
            for j in range(i):
                if sorted_envelope[j][1] < y: 
                    dp[i] = max([dp[i],dp[j]+1])

        return max(dp)
```


# Code2 基于二分法的动态规划
- 时间复杂度: $O(nlogn)$
- 空间复杂度: $O(n)$
```Python []

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        sorted_envelope = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        # 在排序键函数 lambda x: (x[0], -x[1]) 中，元组 (x[0], -x[1]) 指定了两级排序。首先，它按照 x 值进行排序，然后在 x 相同时按照 y 值进行排序。
        n = len(envelopes)
        
        f = [sorted_envelope[0][1]]

        for i in range(1,n):
            num = sorted_envelope[i][1]    
            if num > f[-1]: 
                f.append(num)
            else:
                index = bisect.bisect_left(f,num)
                f[index] = num

        return len(f)
```

