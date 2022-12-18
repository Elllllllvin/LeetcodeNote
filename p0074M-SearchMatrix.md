> Problem: [74. 搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix/description/)

# 解题方法

> 比较简单的两次二分查找

# 注意

python 中的 in 函数的时间复杂度：

- list:O(n)
- dic/set:O(1)

# 复杂度

- 时间复杂度: $O(logn+logm)$

- 空间复杂度: $O(1)$

# Code

```Python []

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1
        while(l<=r):
            mid = (l+r)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                ll,rr = 0,len(matrix[0])-1
                while(ll<=rr):
                    mmid = (ll+rr)//2
                    print(ll,rr,mmid)
                    if matrix[mid][mmid]==target:
                        return True
                    elif matrix[mid][mmid]<target:
                        ll = mmid + 1
                    elif matrix[mid][mmid]>target:
                        rr = mmid - 1
                return False
            elif target<matrix[mid][0]:
                r = mid - 1
            elif target>matrix[mid][-1]:
                l = mid + 1

        return False

```
