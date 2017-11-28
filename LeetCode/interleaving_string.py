"""
-------------------------------
File name    :  interleaving_string.py
Description  :  Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
                For example,
                Given:
                s1 = "aabcc",
                s2 = "dbbca",
                When s3 = "aadbbcbcac", return true.
                When s3 = "aadbbbaccc", return false.
Author       :  钟寰
Time         :  2016/12/24 18:07
---------------------------------
"""


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """设状态{matched[i][j]}，表示{s1[0,i]}和{s2[0,j]}，匹配{s3[0, i+j]}。
        如果s1的最后一个字符等于s3的最后一个字符，则{matched[i][j]=matched[i-1][j]}；
        如果s2的最后一个字符等于s3的最后一个字符，则{matched[i][j]=matched[i][j-1]}。
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n,m,r = len(s1),len(s2),len(s3)
        if n + m != r:
            return False
        matched = [[True for i in range(m+1)] for j in range(n+1)]
        for i in range(1,n+1):              # len(s2) = 0
            matched[i][0] = matched[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1,m+1):              # len(s1) = 0
            matched[0][j] = matched[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1,n+1):
            for j in range(1,m+1):
                matched[i][j] = (matched[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                                (matched[i][j-1] and s2[j-1] == s3[i+j-1])
        return matched[-1][-1]
