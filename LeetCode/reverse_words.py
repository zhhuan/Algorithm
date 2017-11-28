"""
-----------------------
File name   : reverse_words.py
Description : Given an input string, reverse the string word by word.
              For example,
              Given s = "the sky is blue",
              return "blue is sky the".
Author      : 钟寰
Time        : 2016-12-23 15:13
-----------------------
"""

class Solution(object):
    def reverse_words(self,s):
        """
        args:
            type s: str
        returns
            return type: str
        """
        words = s.split()
        return ' '.join(reversed(words))
