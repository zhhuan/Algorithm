"""
-------------------------------
File name    :  min_spanning_tree.py
Description  :  用Prim算法和Kruskal求解最小生成树问题，(A-B,4)表示A点到B点，距离为4
Author       :  钟寰
Time         :  2016/11/30
---------------------------------
"""
import time
from collections import defaultdict
from heapq import *


def mst_prim(vertexs,edges):
    adjacent_vertex = defaultdict(list)
    for v1,v2,length in edges:
        adjacent_vertex[v1].append((length,v1,v2))
        adjacent_vertex[v2].append((length,v2,v1))

    mst=[]
    used = {vertexs[0]}
    usable_edges = adjacent_vertex[vertexs[0]]
    heapify(usable_edges)
    while usable_edges:
        w,v1,v2 = heappop(usable_edges)
        if v2 not in used:
            used.add(v2)
            mst.append((v1,v2,w))
            for next_vertex in adjacent_vertex[v2]:
                heappush(usable_edges,next_vertex)
    return mst


if __name__=='__main__':
    time_start = time.clock()
    vertexs = list("ABCDEFG")
    edges = [("A", "B", 7), ("A", "D", 5),
             ("B", "C", 8), ("B", "D", 9),
             ("B", "E", 7), ("C", "E", 5),
             ("D", "E", 15), ("D", "F", 6),
             ("E", "F", 8), ("E", "G", 9),
             ("F", "G", 11)]
    print('edges:',edges)
    print('prim:',mst_prim(vertexs,edges))

    time_end = time.clock()
    print('time:',time_end-time_start)


# def popmin(pqueue):
#     # A (ascending or min) priority queue keeps element with
#     # lowest priority on top. So pop function pops out the element with
#     # lowest value. It can be implemented as sorted or unsorted array
#     # (dictionary in this case) or as a tree (lowest priority element is
#     # root of tree)
#     lowest = 1000
#     keylowest = None
#     for key in pqueue:
#         if pqueue[key] < lowest:
#             lowest = pqueue[key]
#             keylowest = key
#     del pqueue[keylowest]
#     return keylowest
#
#
# def prim(graph, root):
#     pred = {}  # pair {vertex: predecesor in MST}
#     key = {}  # keep track of minimum weight for each vertex
#     pqueue = {}  # priority queue implemented as dictionary
#
#     for v in graph:
#         pred[v] = -1
#         key[v] = 1000
#     key[root] = 0
#     for v in graph:
#         pqueue[v] = key[v]
#
#     while pqueue:
#         u = popmin(pqueue)
#         for v in graph[u]:  # all neighbors of v
#             if v in pqueue and graph[u][v] < key[v]:
#                 pred[v] = u
#                 key[v] = graph[u][v]
#                 pqueue[v] = graph[u][v]
#     return pred
#
#
# graph = {0: {1: 6, 2: 8},
#          1: {4: 11},
#          2: {3: 9},
#          3: {},
#          4: {5: 3},
#          5: {2: 7, 3: 4}}
#
# pred = prim(graph, 0)
# for v in pred: print
# "%s: %s" % (v, pred[v])
#
# python
# graph.py
# 0: -1
# 1: 0
# 2: 0
# 3: 2
# 4: 1
# 5: 4