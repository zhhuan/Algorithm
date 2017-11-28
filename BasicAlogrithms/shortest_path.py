"""
-------------------------------
File name    :  shortest_path.py
Description  :  用Dijkstra方法求解最短路径，路径权重为正
Author       :  钟寰
Time         :  2016/12/3
---------------------------------
"""
import sys
from heapq import *

class Vertex(object):
    def __init__(self,node):
        self._id = node
        self._distance = sys.maxsize
        self._previous = None
        self.adjacent = {}
        self.visited = False

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.distance == other.distance
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.distance < other.distance
        return NotImplemented

    @property
    def id(self):
        return self._id

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self,dist):
        self._distance = dist

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, prev):
        self._previous = prev

    def add_neighbor(self,neighbor,weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_visited(self):
        self.visited = True


class Graph(object):
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        self.vert_dict[node] = Vertex(node)

    def get_vertex(self,node):
        if node in self.vert_dict:
            return self.vert_dict[node]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

    def get_vertices(self):
        return self.vert_dict.keys()


def dijkstra(graph,start):
    start.distance = 0             #Set the distance for the start node to zero
    unvisited_queue = []  #Put tuple pair into the priority queue
    for v in graph:
        heappush(unvisited_queue,(v.distance,v))

    while len(unvisited_queue):
        current = heappop(unvisited_queue)[1]
        current.set_visited()

        for next in current.adjacent:
            if next.visited:
                continue
            new_dist = current.distance + current.get_weight(next)

            if new_dist < next.distance:
                next.distance = new_dist
                next.previous = current
                print('updated : current = {0} next = {1} new_dist = {2}' \
                .format(current.id, next.id, next.distance))
            else:
                print
                ('not updated : current = {0} next = {1} new_dist = {2}' \
                .format(current.id, next.id, next.distance))


if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')
    print(g.get_vertices())

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('b', 'a', 5)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)
    for v in g.vert_dict:
        print(v)
    dijkstra(g,g.vert_dict['a'])
