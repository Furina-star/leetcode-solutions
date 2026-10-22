"""
Linked List Cycle = Brute Force Approach
Algorithm: Hash Set
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head

        while current is not None:
            if current in visited:
                return True

            visited.add(current)
            current = current.next

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
