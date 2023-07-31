> Problem: [219. 存在重复元素 II](https://leetcode.cn/problems/contains-duplicate-ii/description/)

[TOC]

# 思路
> 我自己的方法：滑动窗口，但是好慢，，，，，

# Code
```Python []

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = []
        if k == 0:
            return False
        for i in range(len(nums)):
            if nums[i] in l:
                return True
            if len(l)<k:
                l.append(nums[i])
            else:
                l.pop(0)
                l.append(nums[i])
            
        return False
        

```

# Code2 Hash表法，很快啊，啪的一下就做出来了
```Python []
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ind = {}
        for i in range(len(nums)):
            if nums[i] not in ind:
                ind[nums[i]] = i
            else:
                diff = i - ind[nums[i]]
                if diff>k:
                    ind[nums[i]] = i
                else:
                    return True

        return False 

```
