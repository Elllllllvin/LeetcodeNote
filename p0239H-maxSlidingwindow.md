> Problem: [239. 滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/description/)

[TOC]
用单调队列

# Code1
```Python []

# class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # 如果数组为空或 k = 0，直接返回空
        if not nums or not k:
            return []
        # 如果数组只有1个元素，直接返回该元素
        if len(nums) == 1:
            return [nums[0]]

        # 初始化队列和结果，队列存储数组的下标
        queue = []
        res = []

        for i in range(len(nums)):
            # 如果当前队列最左侧存储的下标等于 i-k 的值，代表目前队列已满。
            # 但是新元素需要进来，所以列表最左侧的下标出队列
            if queue and queue[0] == i - k:
                queue.pop(0)

            # 对于新进入的元素，如果队列前面的数比它小，那么前面的都出队列
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            # 新元素入队列
            queue.append(i)

            # 当前的大值加入到结果数组中
            if i >= k-1:
                res.append(nums[queue[0]])

        return res

# Code2

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 1:
            return nums
        ans = []
        queue = collections.deque()
        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

        n = len(nums)
        ans.append(nums[queue[0]])
        for i in range(k, n):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

            while queue and queue[0] <= i - k:
                queue.popleft()
            
            ans.append(nums[queue[0]])
        return ans


"""
解析：用队列保存，使得队列中的元素大小按照单调递减排列
1. 设m为当前位置，如果m前面有元素比nums[m]小，那么这个（小）元素永无出头之日，可以直接删除了
2. 但是在m后面的比其小的元素还有出头机会，所以直接append;
即：
3. 循环判断队列最后一个元素nums[queue[-1]]和nums[i]的大小关系:
    nums[i]更大则删除queue[-1]，然后将i放入queue;
    nums[queue[-1]]更大则直接将i放入；
4. 此时的滑动窗口最大元素为nums[queue[0]]，当然还需要保证queue[0]在窗口内，即：queue[0]<=i-k,则删除 
"""


```
