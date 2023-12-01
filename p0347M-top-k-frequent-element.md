> Problem: [347. 前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/description/)

[toc]

# 思路

> 法一：使用Counter()，python独有
> 法二：使用heapq
> 法三：手撕最小堆

# 复杂度

- 时间复杂度: Counter.most_common(k)方法使用的是最小堆（min heap）数据结构，时间复杂度为O(nlogk)

- 空间复杂度: 堆和dic的大小都为$O(n)$

# Code1 Counter

```Python

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Count = collections.Counter(nums)
        res_tuple = Count.most_common(k)
        res = []
        for item in res_tuple:
            res.append(item[0])
        return res
```
# Code2 heapq
```Python []

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Count = collections.Counter(nums)
        hp = []
        for key,val in Count.items():
            heapq.heappush(hp,(val,key))
            while len(hp)>k:
                heapq.heappop(hp)
        # print(hp)            
        
        return [x[1] for x in hp]
```
# Code3 手撕最小堆
```Python
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if (
            left_child_index < len(self.heap)
            and self.heap[left_child_index] < self.heap[smallest]
        ):
            smallest = left_child_index

        if (
            right_child_index < len(self.heap)
            and self.heap[right_child_index] < self.heap[smallest]
        ):
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def size(self):
        return len(self.heap)

# 使用示例
min_heap = MinHeap()
min_heap.push(4)
min_heap.push(2)
min_heap.push(7)
min_heap.push(1)
min_heap.push(9)

print("Min Heap:")
while min_heap.size() > 0:
    print(min_heap.pop())

```
