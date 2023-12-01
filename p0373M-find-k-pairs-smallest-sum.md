> Problem: [373. 查找和最小的 K 对数字](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/description/)

[toc]

# 思路

> 不会啊啊啊啊！！看解析！！！！

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度:

> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度:

> 添加空间复杂度, 示例： $O(n)$

# Code

```Python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        ans = []
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        while pq and len(ans) < k:
            _, i, j = heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans


```
