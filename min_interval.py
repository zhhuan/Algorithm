"""
-------------------------------
File name    :  min_interval.py
Description  :  Given a collection of intervals,find the minimum number of intervals
                you need to remove to make the rest of the intervals non-overlapping
Author       :  钟寰
---------------------------------
"""


class Interval(object):

    def __init__(self,start=0,end=0):
        self.start = start
        self.end = end


def init_intervals(intervals_in):
    """初始化控制台输入的intervals列表，并按interval的end排序

    :param intervals_in:the list of intervals like [[1,2],[2,3]...]
    :return: list[Intervals]
    """
    intervals = [Interval(item[0],item[1]) for item in intervals_in]
    return sorted(intervals,key = lambda item:item.end)


def search_intervals(intervals):
    """利用迭代找出能够容纳最多non-overlapping intervals的方案

    :param intervals:list(Intervals)
    """
    col_intervals = []
    cur = Interval()
    for i in range(len(intervals)):
        if intervals[i].start >= cur.end:
            col_intervals.append(intervals[i])
            cur = intervals[i]
    return col_intervals


if __name__=='__main__':
    interval_num = int(input())
    intervals_in = []
    for i in range(interval_num):
        start_and_end = input()
        intervals_in.append([int(item) for item in start_and_end.split()])
    intervals = init_intervals(intervals_in)
    col_intervals = search_intervals(intervals)
    print(interval_num - len(col_intervals))
