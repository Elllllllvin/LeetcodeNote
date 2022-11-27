_Italic_> Problem: [1. 两数之和](https://leetcode.cn/problems/two-sum/description/)

# Code1: 暴力枚举法

直接循环遍历数组，最先想到的方法&最蠢的方法

- 时间复杂度:

  > 添加时间复杂度, 示例： $O(n^2)$

  - 击败 20.87%

```Python []

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    res = [i,j]
        return res
```

# Code2: 求差前找法

先对于某元素求差，如果求得的差在该元素之前的数组切片内，则输出结果，方法要好于上一种，时间复杂度降了非常多

- 时间复杂度:

  > 添加时间复杂度, 示例： $O(n)$

  - 击败 55.86%

```Python []
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in nums[:i]:
                res = [nums[:i].index(dif),i]
        return res
```

# Code3: 哈希法

仍然求差，但是不再使用切片和 index 操作，因为 index 查找操作也需要 O(n)的时间进行操作，因此使用 Hash 表操作，利用字典表示 hash 表，空间换时间

- 时间复杂度:

  > 添加时间复杂度, 示例： $O(n)$

  - 击败 73.57%

```Python []
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_hash = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in num_hash:
                res = [num_hash[dif],i]
            num_hash[nums[i]] = i
        return res
```
