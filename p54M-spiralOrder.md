> Problem: [54. 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/description/)

# 思路

> 1.按层模拟（Code1，Code2） 2.西瓜削皮（Code3）

# Code1 自己想的方法 ，表达不清楚

```Python []

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m,n =len(matrix[0]),len(matrix)
        if m == 1 :
            for i in range(n):
                res += matrix[i]
            return res
        elif n == 1:
            return matrix[0]
        else:
            k=0
            if n%2 == 0:
                ran = n//2
            else:
                ran = n//2 + 1
            for k in range(ran):
                i = j = k
                while(j<m-k):
                    res.append(matrix[i][j])
                    j +=1
                    if len(res) == m*n:
                        return res
                j -= 1
                i = k+1
                while(i<n-k):
                    print(i,j)
                    res.append(matrix[i][j])
                    if len(res) == m*n:
                        return res
                    i +=1
                i -= 1
                j -= 1
                while(j>=k):
                    res.append(matrix[i][j])
                    if len(res) == m*n:
                        return res
                    j -= 1
                j += 1
                i -= 1
                while(i>k):
                    res.append(matrix[i][j])
                    if len(res) == m*n:
                        return res
                    i -= 1 #i = 0,j = 0

            return res[:m*n]
```

# Code2 好清楚啊，明明设四个值就能说清楚，，，，，

```Python []
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order
```

# Code3 西瓜削皮（结合之前的 p48 旋转矩阵）

```Python []
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            # 削头（第一层）
            res += matrix.pop(0)
            # 将剩下的逆时针转九十度，等待下次被削
            matrix = list(zip(*matrix))[::-1]
        return res
```
