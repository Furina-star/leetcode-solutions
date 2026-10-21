"""
Happy Number = Optimized Approach
Algorithm: Floyd Cycle Detection
Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number: int) -> int:
            total_sum = 0

            while number > 0:
                quotient = number // 10
                remainder = number % 10
                total_sum += remainder ** 2
                number = quotient

            return total_sum

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1

def main():
    n = 10

    solution = Solution()
    result = solution.isHappy(n)
    print(result)

if __name__ == "__main__":
    main()