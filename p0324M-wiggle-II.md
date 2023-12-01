
> Problem: [324. 摆动排序2](https://leetcode.cn/problems/wiggle-sort-ii/)
# 解题方法

先把原数组排序，然后切成两段，从后往前一个隔一个填进去，因为后半段数组一定大于前半段数组中的任意一个值，注意判断奇偶

# 复杂度

- 时间复杂度: O(nlogn)
- 空间复杂度：O(n)

# Code

```Python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = sorted(nums)
        
        x = (n+1)//2
        j,k = x - 1 , n - 1

        for i in range(0,n,2):
          nums[i] = arr[j]
          if i + 1 < n:
            nums[i+1] = arr[k]
          j -= 1
          k -= 1
      
```