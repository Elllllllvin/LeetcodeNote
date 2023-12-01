> Problem: [335. 路径交叉](https://leetcode.cn/problems/self-crossing/description/)

[toc]

# 思路

>一共可以归纳为三种情况，见下图

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(1)$

# Code
``` C
/*               i-2
    case 1 : i-1┌─┐
                └─┼─>i
                 i-3
                 
                    i-2
    case 2 : i-1 ┌────┐
                 └─══>┘i-3
                 i  i-4      (i overlapped i-4)

    case 3 :    i-4
               ┌──┐ 
               │i<┼─┐
            i-3│ i-5│i-1
               └────┘
                i-2

*/
```


```Python


  class Solution:

    def isSelfCrossing(self, distance: List[int]) -> bool:

        n = len(distance)

        for i in range(3,n):

            if distance[i]>=distance[i-2] and distance[i-1]<=distance[i-3]:

                return True

            if i>=4 and distance[i-1] == distance[i-3] and distance[i]+distance[i-4] == distance[i-2]:

                return True

            if i>=5 and distance[i-1] <= distance[i-3] and distance[i-2]>distance[i-4] and distance[i]+distance[i-4] >= distance[i-2] and distance[i-1]+distance[i-5]>=distance[i-3]:

                return True

        return False

```
