> Problem: [334. 递增的三元子序列](https://leetcode.cn/problems/increasing-triplet-subsequence/description/)

[toc]

# 思路

> 好难，，，，

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(1)$

# Code 贪心算法

```Python

  class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        first,second = nums[0],float('inf')
        for i in range(1,n): #寻找third
            if nums[i] > second: #如果third比second大，那么就代表找到了
                return True
            else: 
                if nums[i] > first: # 如果first < third < second,那么贪心地将second的值换为third（second肯定在满足条件的范围内越小越好）
                    second = nums[i]
                else: # 如果third < first ,那么third < first <second，此时讲first更新为third，此时的second和老first仍然满足递增关系，如果之后找到了大于second的third，也找到了，如果小于second大于first，那么又可以更新second，如果比现在的first还小，即可再次更新first，以此循环。
                    first = nums[i]
        return False 

```
