"""
给你一个 只包含正整数 的 非空 数组nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        w = sum(nums)
        if w % 2 == 1:
            return False
        # 只要求出背包恰好能够转入一半的物品即可
        t = w // 2
        len_nums = len(nums)
        dp = [[False] * (t + 1) for _ in range(len_nums + 1)]
        for i in range(len_nums + 1):
            dp[i][0] = True  # 背包剩余重量为0 之后的都选择不装即可 也就是将剩余的都放在另一堆里
        for i in range(1, len_nums + 1):
            for j in range(1, t + 1):
                # 如果剩余的背包容量不能装下第i-1个物品 就只能不装 也就是dp[i-1][j]的状态
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 选择 不装 或者装
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        print(dp)
        return dp[len_nums][t]


if __name__ == '__main__':
    s = Solution()
    print(s.canPartition([1, 2, 2, 1]))
