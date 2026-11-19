"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        map = {}

        current = head

        while current:
            map[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            copied = map[current]

            copied.next = map.get(current.next)
            copied.random = map.get(current.random) 

            current = current.next

        return map[head]