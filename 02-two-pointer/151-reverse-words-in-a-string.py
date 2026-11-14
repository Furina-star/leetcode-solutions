"""
Revers Words in a String
Algorithm: Single-pass word extraction, then reverse the word list and join with single spaces
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = []
        current = ""

        for char in s:
            if char == " ":
                if current:
                    word_list.append(current)
                    current = ""
            else:
                current += char

        if current:
            word_list.append(current)

        word_list.reverse()

        return " ".join(word_list)


def main():
    s = "hello"

    solution = Solution()
    result = solution.reverseWords(s)

    print(result)


if __name__ == "__main__":
    main()
