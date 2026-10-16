# Pandas Practice

LeetCode exercises for learning DataFrame creation, inspection, filtering, and transformation with pandas.

[Back to the repository README](../README.md)

## Setup

Use the virtual environment and shared [requirements.txt](../requirements.txt) described in the [root setup instructions](../README.md#setup). No separate requirements file is needed here.

## Exercises

The solution files below are currently empty. Mark an exercise complete after implementing and checking its solution.

| Day | # | Problem | Topic | Status | Solution |
|---|---|---|---|---|---|
| 01 | 2877 | [Create a DataFrame from List](https://leetcode.com/problems/create-a-dataframe-from-list/) | Introduction to Pandas | Planned | [View](01-introduction-to-pandas/day-01-2877-create-a-dataframe-from-list/solution.py) |
| 02 | 2878 | [Get the Size of a DataFrame](https://leetcode.com/problems/get-the-size-of-a-dataframe/) | Introduction to Pandas | Planned | [View](01-introduction-to-pandas/day-02-2878-get-the-size-of-dataframe/solution.py) |

## Organization

Use this layout as new topics and exercises are added:

```text
pandas/
  README.md
  <topic-number>-<topic-name>/
    day-<day>-<problem-id>-<problem-name>/
      solution.py
```

For each exercise:

1. Add a directory and `solution.py` using the naming pattern above.
2. Start the solution with a docstring containing the problem title, `Algorithm:` describing the pandas operations, and time and space complexity.
3. Implement the required function and check it with example DataFrames and relevant edge cases.
4. Add a row to the exercise table and update its status when complete.

To run an implemented exercise with local example code, use its path from the repository root:

```sh
python pandas/01-introduction-to-pandas/day-01-2877-create-a-dataframe-from-list/solution.py
```

## Resources

- [LeetCode: Introduction to Pandas](https://leetcode.com/studyplan/introduction-to-pandas/)
- [Pandas documentation](https://pandas.pydata.org/docs/)
