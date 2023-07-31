> Problem: [295. 数据流的中位数](https://leetcode.cn/problems/find-median-from-data-stream/description/)

[TOC]

# 思路
> 讲述看到这一题的思路

# 解题方法
1. from sortedcontainers import SortedList

# Code1 利用SortedList函数
```Python []

from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.res = SortedList()
        self.length = 0


    def addNum(self, num: int) -> None:
        self.res.add(num)
        self.length += 1


    def findMedian(self) -> float:
        if self.length%2 == 0:
            return (self.res[self.length//2] + self.res[self.length//2 - 1])/2
        else:
            return self.res[self.length//2]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```
