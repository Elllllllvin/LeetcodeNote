> Problem: [128. 最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/description/)

# 思路

> 1.排序+滑动窗口 2.哈希表

# 复杂度

# Code1

- 时间复杂度: $O(nlogn)$
- 空间复杂度: $O(n)$

```Python []

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        cnt = 0
        maxcnt = 0
        # print(nums)
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]+1:
                cnt+=1
            else:
                cnt = 1
            maxcnt = max(maxcnt,cnt)
        return maxcnt
```

# Code2 官方题解

```Python []
class Solution(object):
    def longestConsecutive(self, nums):
        hash_dict = dict()

        max_length = 0
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)

                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length

                hash_dict[num] = 1
                # 主要要更新下面的两个端点的hash值
                hash_dict[num - left] = cur_length
                hash_dict[num + right] = cur_length
                # print(hash_dict)
        return max_length
```
