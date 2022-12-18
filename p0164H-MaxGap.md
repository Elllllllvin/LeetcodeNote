> Problem: [164. 最大间距](https://leetcode.cn/problems/maximum-gap/description/)

[TOC]

# 思路

由于规定时间空间复杂度都必须为 O(n)，因此不能直接用内置 sort 函数（时间复杂度 O(nlogn)），因此需要使用桶排序

# 解题方法

1.将数组中的各个数等距离分配，也就是每个桶的长度相同，也就是对于所有桶来说，桶内最大值减去桶内最小值都是一样的。

$$
    每个桶的长度 = \max{(1,\lfloor \frac{\max{nums} - \min{nums}}{len(nums)-1} \rfloor)}
$$

2.确定桶的数量，桶内的区间均为左开右闭，因此最后加 1 保证数组的最大值也能分到一个桶。

$$
    桶的数量 = \lfloor \frac{\max{nums} - \min{nums}}{每个桶的长度} \rfloor + 1
$$

3.将数组中的数放到一个个桶里面，不断更新更大的（后一个桶元素最小值，剪前一个桶元素最大值），最终得到答案

4.确定每个数对应的桶：

$$
    location = \frac{nums[i]-min(nums)}{每个桶的长度}
$$

# 复杂度

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

# Code

```Python []

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        max_ele = max(nums)
        min_ele = min(nums)
        max_gap = 0

        bucketLength = max(1,(max_ele-min_ele)//(n-1))
        buckets = [ [] for _ in range((max_ele-min_ele)//bucketLength+1) ]

        for i in range(n):
            loc = (nums[i]-min_ele)//bucketLength
            buckets[loc].append(nums[i])

        pre_max = inf
        for i in range(len(buckets)):
            if buckets[i] and pre_max!=inf:
                max_gap = max(max_gap,min(buckets[i])-pre_max)
            if buckets[i]:
                pre_max = max(buckets[i])
        return max_gap


```
