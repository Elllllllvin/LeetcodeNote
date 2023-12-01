> Problem: [381. O(1) 时间插入、删除和获取随机元素 - 允许重复](https://leetcode.cn/problems/insert-delete-getrandom-o1-duplicates-allowed/description/)

[toc]

# 思路

> 讲述看到这一题的思路

# 解题方法

> 描述你的解题方法

# 复杂度

时间复杂度:

集合（Set）
- add() 函数的时间复杂度：平均情况下为 O(1)，最坏情况下为 O(n)。
- remove() 函数的时间复杂度：**平均情况下为 O(1)**，最坏情况下为 O(n)。
在理想情况下，add() 和 remove() 操作的时间复杂度为 O(1)，因为集合使用哈希表来实现。但在最坏情况下，当发生哈希冲突时，需要解决冲突，可能需要遍历链表或执行其他操作，导致时间复杂度增加到 O(n)。

列表（List）
- append() 函数的时间复杂度：平均情况下为 O(1)，最坏情况下为 O(n)。在最坏情况下，如果列表的空间不足，需要进行动态扩容并复制元素到新的空间，因此时间复杂度会变为 O(n)。
- remove() 函数的时间复杂度：**平均情况下为 O(n)**，因为它需要搜索并删除指定值的元素。如果知道要删除的元素的索引，则可以在 O(1) 时间内删除该元素。
总结：

集合的 add() 和 remove() 操作在平均情况下通常更快，但在最坏情况下可能与列表操作的性能相当或更差。
列表的 append() 操作在大多数情况下是常数时间复杂度，但在需要动态扩容时可能会变为线性时间复杂度。
**列表的 remove() 操作通常需要线性时间复杂度，而集合的 remove() 操作在最坏情况下也可能需要线性时间复杂度。**






空间复杂度: $O(n)$

# Code

```Python

class RandomizedCollection:


    def __init__(self):

        self.dic = collections.defaultdict(list)  

        self.nums = []



    def insert(self, val: int) -> bool:

        self.dic[val].append(len(self.nums))  

        self.nums.append(val)


        return len(self.dic[val]) == 1


    def remove(self, val: int) -> bool:


        if val not in self.dic:

            return False

        else:

            index = self.dic[val].pop() #取得val值在nums中的索引

            last_index = len(self.nums)-1

            self.nums[index] = self.nums[last_index]

            #将nums最后一位元素的值x复制到nums[index]位置中

            if last_index != index:

                self.dic[self.nums[index]].remove(last_index)

                self.dic[self.nums[index]].append(index)

            #现在x在nums中的索引为index，因此更新dic中key为x的值（及x现在在nums中的索引）


            self.nums.pop()

            if len(self.dic[val]) == 0:

                self.dic.pop(val)

            #现在已经把x的值完全移到index位置了，因此可以删除末尾元素，删除nums最后一位，再删除dic中key为val的这个元素。这样，key为val的这个元素就完全remove了

            return True


    def getRandom(self) -> int:

        return random.choice(self.nums)

        # 使用choice随机选择self.nums中的一个元素



# Your RandomizedCollection object will be instantiated and called as such:

# obj = RandomizedCollection()

# param_1 = obj.insert(val)

# param_2 = obj.remove(val)

# param_3 = obj.getRandom()

```
