"""
Linked List Cycle = Optimized Approach
Algorithm: Floyd's Cycle Detection
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if fast is slow:
                return True

        return False

def main():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next

    solution = Solution()
    result = solution.hasCycle(head)

    print(result)

if __name__ == "__main__":
    main()