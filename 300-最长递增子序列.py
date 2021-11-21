'''
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums_len = len(nums)
        dp = [1] * nums_len
        res = 0
        for i in range(nums_len):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(res, dp[j] + 1)
        return max(dp)


class Solution2:
    def __init__(self):
        self.memo = []

    def lengthOfLIS(self, nums: List[int]) -> int:
        self.memo = [-1] * len(nums)
        self.dp(len(nums) - 1, nums)
        print(self.memo)
        return max(self.memo)

    def dp(self, idx, nums):
        if idx == 0:
            self.memo[idx] = 1
            return self.memo[idx]
        if self.memo[idx] != -1:
            return self.memo[idx]
        res = 0
        for i in range(idx):
            # 保证每一个都能得到计算
            tmp = self.dp(i, nums)
            if nums[idx] > nums[i]:
                res = max(res, tmp)
        self.memo[idx] = res + 1
        return self.memo[idx]


if __name__ == '__main__':
    s = Solution2()
    r = s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6])
    print(r)
