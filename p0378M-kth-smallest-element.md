> Problem: [378. 有序矩阵中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/description/)

[toc]

# 思路

> 多路归并排序用最小堆啊啊啊啊啊

# 解题方法

> 最小堆
```python
heapq.heapify(index_pq)  #构建最小堆
heapq.heappush(index_pq, element) #向堆中插入元素
heapq.heappop(index_pq) #弹出顶部元素
```


# 复杂度

- 时间复杂度: $O(n)$  归并k次，每次堆中插入和弹出的操作时间复杂度均为 $\log{n}$。

- 空间复杂度: $O(n)$  最小堆大小始终为n

# Code

```Python


class Solution:

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n = len(matrix)
        index_pq = [(matrix[i][0],i,0) for i in range(n)]
        heapq.heapify(index_pq)

        for i in range(k-1):
            num,x,y = heapq.heappop(index_pq)
            if y != n-1:
                heapq.heappush(index_pq,(matrix[x][y+1],x,y+1))
        return heapq.heappop(index_pq)[0]


```
