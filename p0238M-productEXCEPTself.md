

```python []
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0]*n
        front = [1]*n
        end = [1]*n
        for i in range(n):
            if i == 0:
                front[i] = 1
                end[n-1-i] = 1
            else:
                front[i] = front[i-1]*nums[i-1]
                end[n-1-i] = end[n-1-i+1]*nums[n-1-i+1]
        
        for i in range(n):
            ans[i] = front[i]*end[i]

        return ans

```