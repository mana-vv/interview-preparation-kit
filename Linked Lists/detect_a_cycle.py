"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    temp = []
    while head:
        if head in temp:
            return 1
        if head == None:
            return 0
        temp.append(head)
        head = head.next
        