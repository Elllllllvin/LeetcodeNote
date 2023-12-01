> Problem: [341. 扁平化嵌套列表迭代器](https://leetcode.cn/problems/flatten-nested-list-iterator/description/)

[toc]

# 思路

> 法1:深度优先搜索：，在构造函数中提前「扁平化」整个嵌套列表；
> 法2（重要）：迭代，在调用 hasNext() 或者 next() 方法的时候扁平化当前的嵌套的子列表。

# 复杂度

- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

# Code1 dfs 深度优先搜索

```Python

# """

# This is the interface that allows for creating nested lists.

# You should not implement it, or speculate about its implementation

# """

#class NestedInteger:

#    def isInteger(self) -> bool:

#        """

#        @return True if this NestedInteger holds a single integer, rather than a nested list.

#        """

#

#    def getInteger(self) -> int:

#        """

#        @return the single integer that this NestedInteger holds, if it holds a single integer

#        Return None if this NestedInteger holds a nested list

#        """

#

#    def getList(self) -> [NestedInteger]:

#        """

#        @return the nested list that this NestedInteger holds, if it holds a nested list

#        Return None if this NestedInteger holds a single integer

#        """


class NestedIterator:

    def dfs(self,nestedList):

        for item in nestedList:

            if item.isInteger():

                self.queue.append(item.getInteger())

            else:

                self.dfs(item.getList())



    def __init__(self, nestedList: [NestedInteger]):

        self.queue = []

        self.dfs(nestedList)


    def next(self) -> int:

        return self.queue.pop(0)




    def hasNext(self) -> bool:

        return len(self.queue)>0





# Your NestedIterator object will be instantiated and called as such:

# i, v = NestedIterator(nestedList), []

# while i.hasNext(): v.append(i.next())

```
# Code2  迭代法
```Python []

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for i in range(len(nestedList)-1,-1,-1):  #逆序存入栈中
            self.stack.append(nestedList[i])
    
    def next(self) -> int:
        cur = self.stack.pop()
        return cur.getInteger()
        
    
    def hasNext(self) -> bool:
        if len(self.stack)==0:
            return False
        elif self.stack[-1].isInteger():
            return True
        else:
            while not self.stack[-1].isInteger():
                cur = self.stack.pop()
                cur_list = cur.getList()
                for i in range(len(cur_list)-1,-1,-1):  #逆序存入栈中
                    self.stack.append(cur_list[i])
                if len(self.stack)==0:
                    return False
            return True

        
        

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
```
