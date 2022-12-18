> Problem: [169. 多数元素](https://leetcode.cn/problems/majority-element/description/)

[toc]

# Code 偷个懒

```Python


class Solution:

    def majorityElement(self, nums: List[int]) -> int:

        l = collections.Counter(nums)

        return l.most_common(1)[0][0]

```
