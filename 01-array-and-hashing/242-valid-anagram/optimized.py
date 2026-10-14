"""
Valid Anagram - Optimized Approach
Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = {}
        if len(s) != len(t):
            return False

        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        for char in t:
            if char not in frequency:
                return False

            if frequency[char] == 0:
                return False

            frequency[char] -= 1

        return True


def main():
    s = "anagram"
    t = "nagaram"

    solution = Solution()
    result = solution.isAnagram(s, t)
    print(result)


if __name__ == "__main__":
    main()