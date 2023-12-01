> Problem: [321. 拼接最大数](https://leetcode.cn/problems/create-maximum-number/description/)

[toc]

# 思路

> 讲述看到这一题的思路

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度: pick_max 的时间复杂度为O(M + N)，其中M为nums1的长度，N为nums2的长度。 merge的时间复杂度为O(k)，再加上外层遍历所有的k中可能性。因此总的时间复杂度为O(k^2*(M+N))
- 
空间复杂度：我们使用了额外的 stack 和 ans 数组，因此空间复杂度为 O(max(M, N, k))，其中M为nums1的长度，N为nums2的长度。


# Code

```Python

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max(nums,k):
            stack = []
            drop = len(nums) - k # 需要丢弃掉的数
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]
        
        def merge(A,B):
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger.pop(0))
            return ans

        res = []
        for i in range(k+1):
            if i<=len(nums1) and k-i <= len(nums2):
                res.append(merge(pick_max(nums1,i) , pick_max(nums2,k-i)))
        # print(res)
        return max(res)
        # return max(merge(pick_max(nums1,i) , pick_max(nums2,k-i)) for i in range(k+1) if i<=len(nums1) and k-i <= len(nums2))
        
```
