"""
给定两个单词word1和word2，找到使得word1和word2相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。



示例：

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l = self.lcs(word1, word2)
        return len(word1) - l + len(word2) - l

    def lcs(self, s1: str, s2: str) -> int:
        len_s1 = len(s1)
        len_s2 = len(s2)
        dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[len_s1][len_s2]

        
