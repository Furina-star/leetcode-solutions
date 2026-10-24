
"""
Count Days Spent Together - Brute Force Approach
Algorithm: Day-by-Day Simulation (Linear Scan)
Time Complexity: O(365) = O(1) for a fixed year
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

        count = 0

        for current_day in range(1, 366):
            if (alice_start <= current_day <= alice_end
                    and bob_start <= current_day <= bob_end):
                count += 1

        return count

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
