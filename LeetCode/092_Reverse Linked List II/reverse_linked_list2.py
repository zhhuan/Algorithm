"""
File name   : reverse_linked_list2.py
Description : Reverse a linked list from position m to n. Do it in-place and in one-pass.
            For example:
            Given 1->2->3->4->5->NULL, m = 2 and n = 4,
            return 1->4->3->2->5->NULL.
Author      : 钟寰
Time        : 2017-1-3 23:50
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    def reverseBetween(self, head, m, n):
        prem, pre, next, now, nowm = None, None, None, head, None;
        ind = 1;
        while now is not None:
            next = now.next
            if ind >= m and ind <= n:
                now.next = pre
            if ind == m:
                prem, nowm = pre, now
            if ind == n:
                nowm.next = next
                if prem is None:
                    head = now
                else:
                    prem.next = now
            pre, now, ind = now, next, ind + 1
        return head

