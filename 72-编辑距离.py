import time


class Solution:
    def __init__(self):
        self.memo = {}

    def minDistance(self, word1: str, word2: str) -> int:
        return self.dp(word1, word2, len(word1) - 1, len(word2) - 1)

    def dp(self, s1, s2, i, j):
        key = format("%d-%d" % (i, j))
        if key in self.memo:
            return self.memo[key]
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1

        if s1[i] == s2[j]:
            self.memo[key] = self.dp(s1, s2, i - 1, j - 1)
            return self.memo[key]

        ins_step = self.dp(s1, s2, i, j - 1)
        del_step = self.dp(s1, s2, i - 1, j)
        rep_step = self.dp(s1, s2, i - 1, j - 1)

        res = min(ins_step, del_step, rep_step)
        self.memo[key] = res + 1
        return self.memo[key]


class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = (min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])) + 1
        return dp[m][n]


class Node:
    """
    利用choice保存每个选择的结果
    """

    def __init__(self, val=0, choice=0):
        self.val = val
        self.choice = choice


class Solution3:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[Node(0, 0)] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = Node(i, 0)
        for j in range(n + 1):
            dp[0][j] = Node(j, 0)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = Node(dp[i - 1][j - 1].val,0)
                else:
                    # dp[i][j] = (min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])) + 1
                    # 替换、删除、插入 ==> 1,2,3
                    node, idx = Solution3.min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                    dp_node = Node(node.val + 1, idx)
                    dp[i][j] = dp_node
        for i in range(1, m + 1):
            for j in range(1,n + 1):
                print([dp[i][j].val, dp[i][j].choice], end=' ')
            print()
        return dp[m][n].val

    @staticmethod
    def min(node1: Node, node2: Node, node3: Node):
        if node1.val < node2.val:
            tmp = node1
            idx = 1
        else:
            tmp = node2
            idx = 2
        if tmp.val > node3.val:
            tmp = node3
            idx = 3
        return tmp, idx


if __name__ == '__main__':
    start = time.time()
    s = Solution3()
    # for i in range(1000):
    distance = s.minDistance("horse", "ros")
    print(distance)
    print(time.time() - start)
