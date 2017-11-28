import unittest
from huffman_encode import *

class TestHuffman(unittest.TestCase):

    def test_init(self):
        char_freqs = [1,1,3,5]
        nodes = create_nodes(char_freqs)
        root = create_huffman_tree(nodes)
        self.assertEqual(root.freq,10)


if __name__=='__main__':
    unittest.main()