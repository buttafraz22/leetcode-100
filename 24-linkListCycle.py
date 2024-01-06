# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # This is a classic Floyd's cycle algorithm.
    # We will use a two pointer approach, with both pointers
    # moving at different speeds. If there is a cycle, 
    # it will be detected by the fact that the slow pointer
    # will catch up with the fast one.
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False