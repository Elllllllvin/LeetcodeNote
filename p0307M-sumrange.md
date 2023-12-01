> Problem: [307. 区域和检索 - 数组可修改](https://leetcode.cn/problems/range-sum-query-mutable/description/)

[TOC]

# 思路
> 树状数组

# 解题方法
> 描述你的解题方法

# 复杂度
- 时间复杂度: 
初始化 $O(logn)$
update logn
add logn
sumrange logn

# Code
```Python []

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0]*(len(nums)+1)
        # 构造出的bit空间比原nums多一个，第一个下标0不用
        for i,num in enumerate(nums,1): #i从1开始计数
            self.add(i,num)

    def lowbit(self,x):
        return x & -x

    def query(self,i):
        # 求前缀和
        ans = 0
        while i>0:
            ans += self.tree[i]
            i -= self.lowbit(i)
        return ans
    
    def add(self,i,delta):
        # 在指定的i处+delta
        while i<=self.n:
            self.tree[i] += delta
            i += self.lowbit(i)

    def update(self, index: int, val: int) -> None:
        self.add(index+1,val - self.nums[index])
        self.nums[index] = val


    def sumRange(self, left: int, right: int) -> int:
        return self.query(right+1) - self.query(left+1-1)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
```
