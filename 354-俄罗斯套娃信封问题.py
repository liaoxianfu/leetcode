from typing import List
#
# a = [
#     [1, 2],
#     [2, 3],
#     [2, 5],
#     [-1, 1],
#     [4, -1],
#     [4, 5]
# ]
#
# b = sorted(a, key=lambda x: (x[0], -x[1]))
#
# print(b)


"""
给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。

当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

注意：不允许旋转信封。

 
示例 1：

输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
示例 2：

输入：envelopes = [[1,1],[1,1],[1,1]]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/russian-doll-envelopes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        env_len = len(envelopes)
        env = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        nums = [e[1] for e in env]
        dp = [1] * env_len
        for i in range(1, env_len):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))