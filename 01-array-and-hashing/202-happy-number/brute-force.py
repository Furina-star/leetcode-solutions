"""
Happy Number - Hash Set Approach
Algorithm: Cycle Detection using Hash Set
Time Complexity: O(log n)
Space Complexity: O(log n)
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            total_sum = 0

            while n > 0:
                remainder = n % 10
                total_sum += remainder ** 2
                n //= 10

            n = total_sum

        return True

def main():
    n = 19

    solution = Solution()
    result = solution.isHappy(n)
    print(result)

if __name__ == "__main__":
    main()