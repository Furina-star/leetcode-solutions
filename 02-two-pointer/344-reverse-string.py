"""
Reverse String
Algorithm: Reverse Method
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()

def main():
    s = ["h","e","l","l","o"]

    solution = Solution()
    solution.reverseString(s)

    print(s)

if __name__ == "__main__":
    main()