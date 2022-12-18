> Problem: [167. 两数之和 II - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/)

# 思路

1.暴力法 2.左右指针

# Code1 暴力法

- 时间复杂度: $O(n^2)$
- 空间复杂度: $O(1)$

```Python []

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            if i>0 and numbers[i] == numbers[i-1]:
                continue
            for j in range(i+1,n):
                if numbers[i]+numbers[j] == target:
                    return [i+1,j+1]
```

# Code2 双指针法

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

```Python []

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l,r = 0,n-1
        while(l<r):
            if l>0 and numbers[l] == numbers[l-1]:
                l += 1
                continue
            if r<n-1 and numbers[r] == numbers[r+1]:
                r -= 1
                continue
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
```
