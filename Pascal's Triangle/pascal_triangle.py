"""
Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
Return 
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


"""
#@author zhonghuan
#@data 2016/4/17
class MySolution(object):
    def generate(self, numRows):
        """
        :type numRows:int
        :rtype:List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            last_list = [1,1]
            ret_list = [[1],[1,1]]
            for i in range(2,numRows):
                cur_list = list(range(i+1))
                cur_list[0] = 1
                cur_list[i] = 1
                for index in range(1,i):
                    cur_list[index] = last_list[index-1]+last_list[index]
                last_list = cur_list
                ret_list.append(cur_list)
            return ret_list
"""
others
runtime :48ms
class Solution(object):
    def generate(self, numRows):
        if not numRows: return []
        ret = [[1]]
        numRows -= 1
        while numRows:
            ret.append([1] + [a+b for a,b in zip(ret[-1][:-1], ret[-1][1:])] +[1])
            numRows-=1
        return ret

"""
