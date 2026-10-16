"""
Ransom Note - Brute Force Approach
Algorithm: Nested Loops
Time complexity: O(m * n), where m is the length of magazine and n is the length of ransomNote
Space complexity: O(m)
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        used = [False] * len(magazine)

        for char in ransomNote:
            found = False

            for i in range(len(magazine)):
                if magazine[i] == char and not used[i]:
                    used[i] = True
                    found = True
                    break

            if not found:
                return False

        return True

def main():
    ransomNote = "a"
    magazine = "aab"

    solution = Solution()
    result = solution.canConstruct(ransomNote, magazine)

    print(result)

if __name__ == "__main__":
    main()