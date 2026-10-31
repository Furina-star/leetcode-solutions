"""
Move Zeroes
Algorithm: Two Pointers (Read and Write)
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                if read != write:
                    nums[read], nums[write] = nums[write], nums[read]

                write += 1

def main():
    nums = [0,0,0,3,12]

    solution = Solution()
    solution.moveZeroes(nums)

    print(nums)

if __name__ == "__main__":
    main()
