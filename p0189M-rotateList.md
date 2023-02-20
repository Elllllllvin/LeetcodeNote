_Italic_> Problem: [189. 轮转数组](https://leetcode.cn/problems/rotate-array/description/)

# 思路

法 1：暴力轮转法：一个一个换，但是会超时，只能过 34/38
法 2：辅助数组法：能过，但是 O(n)空间复杂度
法 3: python 复制法，要写成`nums[:] = nums[-1*k:]+nums[:-1*k]`才能赋值成功!,不能写`nums = nums[-1*k:]+nums[:-1*k]`

# Code1: 暴力轮转法

- 时间复杂度: $O(n*k)$
- 空间复杂度: $O(1)$

```Python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k%len(nums)):
            temp = nums[-1]
            for j in range(len(nums)-1,-1,-1):
                nums[j] = nums[j-1]
            nums[0] = temp
```

# Code2: 辅助数组法

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

```Python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        res = nums[-1*k:]+nums[:-1*k]
        for i in range(len(nums)):
            nums[i] = res[i]

```

# Code3: python 复制法

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

```Python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        nums[:] = nums[-1*k:]+nums[:-1*k]
```
