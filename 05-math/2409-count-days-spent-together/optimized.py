"""
Count Days Spent Together - Optimized Approach
Algorithm: Day-of-Year Conversion + Interval Intersection
Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [
            31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31
        ]

        def day_of_year(date: str) -> int:
            month, day = map(int, date.split("-"))
            return sum(days_in_month[:month - 1]) + day

        alice_start = day_of_year(arriveAlice)
        alice_end = day_of_year(leaveAlice)
        bob_start = day_of_year(arriveBob)
        bob_end = day_of_year(leaveBob)

        overlap_start = max(alice_start, bob_start)
        overlap_end = min(alice_end, bob_end)

        return max(0, overlap_end - overlap_start + 1)

def main():
    arriveAlice = "08-15"
    leaveAlice = "08-18"
    arriveBob = "08-16"
    leaveBob = "08-19"

    solution = Solution()
    result = solution.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob)

    print(result)

if __name__ == "__main__":
    main()