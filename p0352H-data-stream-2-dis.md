> Problem: [352. 将数据流变为多个不相交区间](https://leetcode.cn/problems/data-stream-as-disjoint-intervals/description/)

[toc]

# 思路

关于addNum函数

这段代码是一个用于处理区间集合的类的方法 `addNum` 的实现，该方法用于将一个整数值 `val` 添加到区间集合中。这个区间集合以字典的形式表示，其中键表示区间的左边界，值表示区间的右边界。这个方法的主要目标是维护区间集合，确保不会出现重叠的区间，并根据不同情况来更新区间。

下面是代码的主要逻辑：

1. `intervals_ = self.intervals`：首先，将类成员变量 `self.intervals` 赋值给局部变量 `intervals_`，以便更方便地访问区间集合。
2. `keys_ = self.intervals.keys()` 和 `values_ = self.intervals.values()`：创建两个列表，`keys_` 包含区间集合的左边界，`values_` 包含区间集合的右边界。这将用于后续的操作。
3. `interval1` 和 `interval0` 的计算：这两个变量用于查找满足特定条件的区间，具体操作如下：

   - `interval1`：找到 `val` 大于区间左边界的最小区间。如果没有这样的区间，`interval1` 设置为 `len(intervals_)`，表示 `val` 在所有区间之后。
   - `interval0`：找到 `val` 大于等于区间左边界的最大区间。如果没有这样的区间，`interval0` 设置为 `len(intervals_)`，表示 `val` 在所有区间之前。
4. 根据情况更新区间集合：根据 `interval0` 和 `interval1` 找到的区间，以及其他条件，执行不同的更新操作。这些操作包括：

   - 情况一：如果 `val` 在某个区间内，无需进行任何操作，直接返回。
   - 情况二：如果 `val` 与某个区间的左边界相邻，将该区间的左边界增加1。
   - 情况三：如果 `val` 与某个区间的右边界相邻，将该区间的右边界减小1。
   - 情况四：如果 `val` 既与左边界相邻又与右边界相邻，将两个区间合并为一个。
   - 情况五：如果 `val` 与任何现有区间都没有交集，创建一个新的区间，左右边界都为 `val`。

这个方法的目的是保持区间集合的不重叠性，并根据不同情况更新区间。这种数据结构和算法通常用于处理区间的合并和查找操作。

# 解题方法

> 描述你的解题方法

# 复杂度

- 时间复杂度:  $O(n)$
- 空间复杂度:  $O(n)$

# Code

```python


from sortedcontainers import SortedDict

class SummaryRanges:


    def __init__(self):

        self.intervals = SortedDict()


    def addNum(self, value: int) -> None:

        interval = self.intervals

        keys = self.intervals.keys()

        vals = self.intervals.values()


        #   找到 l1 最小的且满足 l1 > val 的区间 interval1 = [l1, r1]

        #   如果不存在这样的区间，interval1 为 len(intervals)

        interval1 = interval.bisect_right(value)


        #   找到 l0 最大的且满足 l0 < val 的区间 interval0 = [l0, r0]

        #   如果不存在这样的区间，interval0 为尾迭代器

        interval0 = (len(interval) if interval1 == 0 else interval1 - 1)


        if interval0 != len(interval) and keys[interval0] <= value <= vals[interval0]:

            # 情况一

            return

        else:

            left_aside = (interval0 != len(interval) and vals[interval0] + 1 == value)

            right_aside = (interval1 != len(interval) and keys[interval1] - 1 == value)

            if left_aside and right_aside:

                # 情况四

                left, right = keys[interval0], vals[interval1]

                interval.popitem(interval1)

                interval.popitem(interval0)

                interval[left] = right

            elif left_aside:

                # 情况二

                interval[keys[interval0]] += 1

            elif right_aside:

                # 情况三

                right = vals[interval1]

                interval.popitem(interval1)

                interval[value] = right

            else:

                # 情况五

                interval[value] = value







    def getIntervals(self) -> List[List[int]]:

        return list(self.intervals.items())




# Your SummaryRanges object will be instantiated and called as such:

# obj = SummaryRanges()

# obj.addNum(value)

# param_2 = obj.getIntervals()

```
