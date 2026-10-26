<h1 align="center">LeetCode Solutions</h1>

<p align="center">
A personal repository for practicing LeetCode algorithms and pandas exercises using Python.
</p>

<p align="center">
The repository tracks my progress, implementations, and improvements in algorithmic efficiency.
</p>

<p align="center">
  <a href="https://leetcode.com/"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=flat&amp;logo=leetcode&amp;logoColor=black" alt="LeetCode"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3-3776AB?style=flat&amp;logo=python&amp;logoColor=white" alt="Python 3"></a>
  <a href="pandas/README.md"><img src="https://img.shields.io/badge/pandas-150458?style=flat&amp;logo=pandas&amp;logoColor=white" alt="pandas exercises"></a>
  <a href="#progress"><img src="https://img.shields.io/badge/Algorithms%20Solved-19-2EA44F?style=flat" alt="Algorithm problems solved: 19"></a>
</p>

## Progress

**Language:** Python 3  
**Algorithm Problems Solved:** 19

Pandas exercises and their status are tracked in the [pandas README](pandas/README.md).

| # | Problem | Difficulty | Topic | Solution |
|---|---|---|---|---|
| 001 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Array & Hashing | [View](01-array-and-hashing/001-two-sum/) |
| 009 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy | Math | [View](05-math/009-palindrome-number/) |
| 053 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | Dynamic Programming | [View](03-dynamic-programming/053-maximum-subarray/) |
| 070 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | Dynamic Programming | [View](03-dynamic-programming/070-climbing-stairs/) |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | Array & Hashing | [View](01-array-and-hashing/121-best-time-to-buy-and-sell-stock/) |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Two Pointers | [View](02-two-pointer/125-valid-palindrome/) |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Linked List | [View](04-linked-list/141-linked-list-cycle/) |
| 167 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | Two Pointers | [View](02-two-pointer/167-two-sum-ii/) |
| 202 | [Happy Number](https://leetcode.com/problems/happy-number/) | Easy | Array & Hashing | [View](01-array-and-hashing/202-happy-number/) |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Array & Hashing | [View](01-array-and-hashing/217-contains-duplicate/) |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Array & Hashing | [View](01-array-and-hashing/242-valid-anagram/) |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | Two Pointers | [View](02-two-pointer/283-move-zeroes/) |
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Easy | Two Pointers | [View](02-two-pointer/344-reverse-string/) |
| 383 | [Ransom Note](https://leetcode.com/problems/ransom-note/) | Easy | Array & Hashing | [View](01-array-and-hashing/383-ransom-note/) |
| 387 | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | Easy | Array & Hashing | [View](01-array-and-hashing/387-first-unique-character/) |
| 565 | [Array Nesting](https://leetcode.com/problems/array-nesting/) | Medium | Array & Hashing | [View](01-array-and-hashing/565-array-nesting/) |
| 1254 | [Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/) | Medium | Graphs | [View](06-graphs/1254-number-of-closed-islands/) |
| 2409 | [Count Days Spent Together](https://leetcode.com/problems/count-days-spent-together/) | Easy | Math | [View](05-math/2409-count-days-spent-together/) |
| 3619 | [Count Islands with Total Value Divisible by K](https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/) | Medium | Graphs | [View](06-graphs/3619-count-islands-with-total-value-divisble-by-k/) |

## Repository Structure

| Directory | Contents |
|---|---|
| [01-array-and-hashing/](01-array-and-hashing/) | Array and hashing problems |
| [02-two-pointer/](02-two-pointer/) | Two-pointer problems |
| [03-dynamic-programming/](03-dynamic-programming/) | Dynamic programming problems |
| [04-linked-list/](04-linked-list/) | Linked list problems |
| [05-math/](05-math/) | Math problems |
| [06-graphs/](06-graphs/) | Graph problems |
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
