> Problem: [41. 缺失的第一个正数](https://leetcode.cn/problems/first-missing-positive/description/)

# Code1 自己做的

偷懒用了 sort 函数，但是 py 内置的 sort 函数时间复杂度为 $O(nlogn)$，空间复杂度为 $O(1)$

```Python []

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if 1 not in nums:
            return 1
        start = nums.index(1)
        res = nums[start]
        for i in range(start+1,len(nums)):
            if nums[i]>nums[i-1] and nums[i] - nums[i-1] != 1:
                res = nums[i-1]
                break
            else:
                res = nums[i]
            print(res)
        res += 1
        return res
```

# Code2 Hash 表变种（官方）

```Python []
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 把所有小于等于0的数先改成n+1
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # 长度为N的数组，答案一定在1~N中，如果 1~N都出现，则答案为n+1，出现就做符号标记
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        # 找第一个非负数的index
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
```
