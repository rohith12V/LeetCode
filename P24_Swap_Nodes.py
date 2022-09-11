# Definition for singly-linked list.
from calendar import c
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # Approach - 1
    # Store Nodes in Stack
    # Tc - O(2n)
    # Sc - O(n)

    # if len == even ( pop last 3 elements and swap using last_Node as last element)
    # if len == odd ( pop last 2 elements and swap using last_Node as None)
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Stack to store the vertices
        trace = []
        len = 0

        # traversal - O(n)
        while head:
            trace.append(head)
            head = head.next
            len += 1

        # if len == odd last_node will point to last element else None
        last_node = None
        if len % 2 != 0:
            last_node = trace.pop()
            len -= 1

        # Perform poping and swapping the addresses
        while len > 0:
            a_ptr = trace.pop()
            b_ptr = trace.pop()
            b_ptr.next = last_node
            a_ptr.next = b_ptr
            last_node = a_ptr
            len -= 2

        # return pointer
        return last_node

    # Approach - 2
    # Using Dummy Node
    # Tc - O(n)
    # Sc - O(1)
    def swapPairsV1(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Dummy Node
        dummy_node = ListNode(-1)

        # -1 (prev)  ---> 1 ( current ) --> 2 --> 3 ---> 4
        dummy_node.next = head
        previous = dummy_node
        current = head

        # Swap logic
        while current != None and current.next != None:
            # Exhange Pointers
            # -1 (prev)   1 ( current ) --> 2 --> 3 ---> 4
            #       |______________________|
            previous.next = current.next

            # -1 (prev)   1 ( current ) --> 2 --> 3 ---> 4
            #       |______|________________|     |
            #              |______________________|
            current.next = previous.next.next

            # -1 (prev)   1 ( current ) <--- 2 --> 3 ---> 4
            #       |______|________________|     |
            #              |______________________|
            previous.next.next = current

            # -1 (prev)--> 2 ---> 1 ( current )---> 3 ---> 4

            # Shift pointers
            previous = current
            current = current.next

            # -1--> 2 ---> 1 ( prev )---> 3 (current) ---> 4

        return dummy_node.next


ob = Solution()
node = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4))))
result = ob.swapPairsV1(node)
print(result)
