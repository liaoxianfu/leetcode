"""

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MIN_VAL = -0xffffff
        len_nums = len(nums)
        dp = [MIN_VAL] * len_nums
        dp[0] = nums[0]
        for i in range(1, len_nums):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)


class Solution2:
    """
    递归写法
    """

    def __init__(self):
        self.MIN_VAL = -0xffffff
        self.res = self.MIN_VAL
        self.nums = []
        self.memo = []

    def maxSubArray(self, nums: List[int]) -> int:
        self.memo = [self.MIN_VAL] * len(nums)
        self.nums = nums
        self.dp(len(nums) - 1)
        return self.res

    def dp(self, idx):
        if self.memo[idx] != self.MIN_VAL:
            print(format("%d命中" % idx))
            self.res = self.memo[idx] if self.res < self.memo[idx] else self.res
            return self.res
        if idx == 0:
            self.memo[idx] = self.nums[0]
            self.res = self.nums[0] if self.res < self.nums[0] else self.res
            return self.nums[0]
        t = max(self.nums[idx], self.nums[idx] + self.dp(idx - 1))
        self.memo[idx] = t
        self.res = t if self.res < t else self.res
        return t


class Solution3:
    """
    状态压缩
    """

    def maxSubArray(self, nums: List[int]) -> int:
        MIN_VAL = -0xffffff
        len_nums = len(nums)
        res = MIN_VAL
        dp_0 = nums[0]
        for i in range(1, len_nums):
            dp_1 = max(nums[i], dp_0 + nums[i])
            res = dp_1 if res < dp_1 else res
            dp_0 = dp_1
        return res


if __name__ == '__main__':
    s = Solution3()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
