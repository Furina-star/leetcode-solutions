# LeetCode Solutions

A personal repository for practicing LeetCode algorithms and pandas exercises using Python.

The repository tracks my progress, implementations, and improvements in algorithmic efficiency.

## Progress

**Language:** Python 3  
**Algorithm Problems Solved:** 9

Pandas exercises and their status are tracked in the [pandas README](pandas/README.md).

| # | Problem | Difficulty | Topic | Solution |
|---|---|---|---|---|
| 001 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Array & Hashing | [View](01-array-and-hashing/001-two-sum/) |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Two Pointers | [View](02-two-pointer/125-valid-palindrome/) |
| 167 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | Two Pointers | [View](02-two-pointer/167-two-sum-ii/) |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Array & Hashing | [View](01-array-and-hashing/217-contains-duplicate/) |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Array & Hashing | [View](01-array-and-hashing/242-valid-anagram/) |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | Two Pointers | [View](02-two-pointer/283-move-zeroes/) |
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Easy | Two Pointers | [View](02-two-pointer/344-reverse-string/) |
| 383 | [Ransom Note](https://leetcode.com/problems/ransom-note/) | Easy | Array & Hashing | [View](01-array-and-hashing/383-ransom-note/) |
| 387 | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | Easy | Array & Hashing | [View](01-array-and-hashing/387-first-unique-character/) |

## Repository Structure

| Directory | Contents |
|---|---|
| [01-array-and-hashing/](01-array-and-hashing/) | Array and hashing problems |
| [02-two-pointer/](02-two-pointer/) | Two-pointer problems |
| [pandas/](pandas/README.md) | Pandas exercises, organized by topic and day |

Algorithm problems use `<topic>/<problem-id>-<problem-name>/`, with `brute_force.py` and `optimized.py` where applicable. Each solution starts with a docstring containing the title, an `Algorithm:` line directly below it, and time and space complexity.

Add new topics to this index and completed algorithm problems to the progress table. Keep pandas exercise details in its own README.

## Setup

From the repository root, create a virtual environment and install the shared dependencies:

```sh
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```sh
source .venv/bin/activate
```

```sh
python -m pip install -r requirements.txt
```

[requirements.txt](requirements.txt) is shared by both tracks and currently lists `pandas`. Algorithm solutions use the Python standard library; pandas exercises use the installed pandas package. Add future third-party dependencies to this root file.

Run a solution from the repository root, for example:

```sh
python 01-array-and-hashing/001-two-sum/optimized.py
```

## Learning Approach

For each problem, I aim to:

1. Understand the problem and its constraints.
2. Develop an initial working solution.
3. Test different inputs and edge cases.
4. Analyze time and space complexity.
5. Optimize the solution when applicable.
6. Document and track my progress.

## Resources

- [LeetCode](https://leetcode.com/)
- [Python Documentation](https://docs.python.org/3/)
