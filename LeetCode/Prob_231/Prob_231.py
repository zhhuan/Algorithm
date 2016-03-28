
'''
Created on 2016年3月28日

@author: zymxq
'''
def isPowerOfTwo(self, n):
    """
    :type n: int
    :rtype: bool
    """
    return n>1 and bin(n).count('1') == 1