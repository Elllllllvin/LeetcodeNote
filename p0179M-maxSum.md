_Italic_> Problem: [179. 最大值](https://leetcode.cn/problems/largest-number/description/)

# 思路

不会做。。。。。自定义排序

# Code 自定义排序

```Python

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = map(str, nums)
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1
        strs = sorted(strs, key=functools.cmp_to_key(cmp), reverse=True)
        return ''.join(strs) if strs[0] != '0' else '0'

```
