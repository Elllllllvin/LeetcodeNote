> Problem: [274. H 指数](https://leetcode.cn/problems/h-index/description/)

[TOC]

# 思路
1.先排序再遍历  O(nlogn)  O(n)
2.二分法

# Code1
```Python []

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        rev_cite = sorted(citations,reverse = True)
        h = 0

        for i in range(len(rev_cite)):
            if rev_cite[i] > h:
                h +=1
            else:
                break

        return h
        
```

# Code2 二分法
```Python []
class Solution:
    def hIndex(self, nums: List[int]) -> int:
        # x篇>=x,则一定x-1篇>=x-1
        # x篇>=x不符合,则一定x+1篇>=x+1不符合
        n=len(nums)
        l,r=1, n # 篇数取值范围
        def ck(x):
            if sum(c>=x for c in nums)>=x:
                return False
            else:
                return True
        while l<=r:
            mid=l+(r-l)//2
            if ck(mid):
                r=mid-1
            else:
                l=mid+1
        return l-1

```
