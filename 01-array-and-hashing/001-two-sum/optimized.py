class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            current = nums[i]
            complement = target - current

            if complement in seen:
                previous_index = seen[complement]
                return [previous_index, i]

            seen[current] = i

def main():

    #Input lists
    nums = [3,2,4]

    # Target sum
    target = 6

    # Calling
    solver = Solution()
    results = solver.twoSum(nums, target)

    print(results)

if __name__ == "__main__":
    main()