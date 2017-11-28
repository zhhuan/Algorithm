"""
-------------------------------
File name    :  HuffmanEncode.py
Description  :  编写了Node类，创建了createNodes、createHuffmanTree、huffmanEncode函数
Author       :  钟寰
---------------------------------
"""
from sys import argv


class Node(object):
    """。

    """
    def __init__(self,freq):
        """创建Node类，初始化结点的左右孩子和父结点"""
        self.left_node = None
        self.right_node = None
        self.father_node = None
        self.freq = freq

    def is_left_node(self):
        return self.father_node.left_node == self


def create_nodes(freqs):
    """添加所有叶子结点"""
    return [Node(freq) for freq in freqs]


def create_huffman_tree(nodes):
    """构建huffman树"""
    queue = nodes[:]
    for i in range(1,len(nodes)):
        queue.sort(key=lambda node:node.freq)    #按照关键字大小排序
        left = queue.pop(0)
        right = queue.pop(0)
        father = Node(left.freq + right.freq)
        left.father_node = father
        right.father_node = father
        father.left_node = left
        father.right_node = right
        queue.append(father)
    return queue[0]


def huffman_encode(nodes,root):
    """对huffman树进行0、1编码"""
    codes = ['']*len(nodes)
    for i in range(len(nodes)):
        tmp_node = nodes[i]
        while tmp_node is not root:
            if tmp_node.is_left_node():
                codes[i] = '0'+codes[i]
            else:
                codes[i] = '1'+codes[i]
            tmp_node = tmp_node.father_node
    return codes


def huffman_price(nodes,root):
    """计算所有叶子的最小总代价
    Min( W1 * L1 + W2 * L2 + W3 * L3 + … + Wn * Ln)
    """
    prices = ['']*len(nodes)
    for i in range(len(nodes)):
        cur_node = nodes[i]
        num = 0
        while cur_node is not root:
            num = num + 1
            cur_node = cur_node.father_node
        prices[i] = num*nodes[i].freq
    return sum(prices)


def test():
    arg = argv
    if len(arg)==1:
        char_freqs = [('f', 5), ('e', 9), ('c', 12), ('b', 13), ('d', 16), ('a', 45)]
        nodes = create_nodes([char_freq[1] for char_freq in char_freqs])
        root = create_huffman_tree(nodes)
        codes = huffman_encode(nodes, root)
        for (item, code) in zip(char_freqs, codes):
            print('Character:%s freq:%d encode:%s' % (item[0], item[1], code))
    elif arg[1] == 'countPrice':
        char_num = int(input())
        freqs_in = input()
        char_freqs = [int(freq) for freq in freqs_in.split()]
        nodes = create_nodes(char_freqs)
        root = create_huffman_tree(nodes)
        print(huffman_price(nodes, root))
    else:
        print('the argument is wrong')


if __name__=='__main__':
    test()



