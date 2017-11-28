"""
-------------------------------
File name    :  matrix_chain.py
Description  :  动态规划解矩阵链乘法问题，得到矩阵相乘次数最少的结合方案（用括号表示）。
Author       :  钟寰
Time         :  2016/11/29
---------------------------------
"""
import sys


class Matrix(object):
    def __init__(self,rows=0,cols=0):
        self.rows = rows
        self.cols = cols


def matrix_chain_order(matrixs):
    matrixs_len = len(matrixs)
    count = [[0 for j in range(matrixs_len)] for i in range(matrixs_len)]
    parens = [[0 for j in range(matrixs_len)] for i in range(matrixs_len)]
    for interval in range(1,matrixs_len+1):
        for i in range(matrixs_len-interval):  #
            j = i+interval
            count[i][j] = sys.maxsize
            for k in range(i,j):
                count_tmp = count[i][k]+count[k+1][j]+matrixs[i].rows*matrixs[i].cols*matrixs[j].cols
                if count_tmp < count[i][j]:
                    count[i][j] = count_tmp
                    parens[i][j] = k
    return parens


def print_optimal_parens(parens,start,end):
    if start == end:
        print('A',end='')
    else:
        print('(',end='')
        print_optimal_parens(parens,start,parens[start][end])
        print_optimal_parens(parens,parens[start][end]+1,end)
        print(')',end='')

if __name__=='__main__':
    matrixs = [Matrix(30,35),Matrix(35,15),Matrix(15,5),Matrix(5,10),Matrix(10,20),Matrix(20,25)]
    parens = matrix_chain_order(matrixs)
    print_optimal_parens(parens,0,5)








