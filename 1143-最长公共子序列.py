"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

 

示例 1：

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.memo = {}
        return self.dp(text1, 0, text2, 0)

    def dp(self, s1, i, s2, j):
        if i == len(s1) or j == len(s2):
            return 0
        key = str(i) + '-' + str(j)
        if key in self.memo:
            return self.memo[key]
        if s1[i] == s2[j]:
            self.memo[key] = 1 + self.dp(s1, i + 1, s2, j + 1)
        else:
            self.memo[key] = max(self.dp(s1, i + 1, s2, j), self.dp(s1, i, s2, j + 1))
        return self.memo[key]


class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1 = text1
        s2 = text2
        len_s1, len_s2 = len(text1), len(text2)
        dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                # 如果相等就在i-1 j-1长度的子字符串基础上+1
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # s1 s2至少有一个不在lcs字符串上
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[len_s1][len_s2]



if __name__ == '__main__':
    s = Solution2()
    print(s.longestCommonSubsequence("abcde", "aace"))
