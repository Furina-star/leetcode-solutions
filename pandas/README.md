# Pandas Practice

LeetCode exercises for learning DataFrame creation, inspection, filtering, and transformation with pandas.

[Back to the repository README](../README.md)

## Setup

Use the virtual environment and shared [requirements.txt](../requirements.txt) described in the [root setup instructions](../README.md#setup). No separate requirements file is needed here.

## Exercises

### Introduction to Pandas

All 15 exercises from the [LeetCode study plan](https://leetcode.com/studyplan/introduction-to-pandas/), stored in [01-introduction-to-pandas/](01-introduction-to-pandas/).

**Exercises Completed:** 9 / 15

Mark an exercise complete after implementing and checking its solution.

| # | Problem | Topic | Status | Solution |
|---|---|---|---|---|
| 2877 | [Create a DataFrame from List](https://leetcode.com/problems/create-a-dataframe-from-list/) | Introduction to Pandas | Completed | [View](01-introduction-to-pandas/2877-create-a-dataframe-from-list/solution.py) |
| 2878 | [Get the Size of a DataFrame](https://leetcode.com/problems/get-the-size-of-a-dataframe/) | Introduction to Pandas | Completed | [View](01-introduction-to-pandas/2878-get-the-size-of-dataframe/solution.py) |
| 2879 | [Display the First Three Rows](https://leetcode.com/problems/display-the-first-three-rows/) | Introduction to Pandas | Completed | [View](01-introduction-to-pandas/2879-display-the-first-three-rows/solution.py) |
| 2880 | [Select Data](https://leetcode.com/problems/select-data/) | Introduction to Pandas | Completed | [View](01-introduction-to-pandas/2880-select-data/solution.py) |
| 2881 | [Create a New Column](https://leetcode.com/problems/create-a-new-column/) | Introduction to Pandas | Completed | [View](01-introduction-to-pandas/2881-create-a-new-column/solution.py) |
| 2882 | [Drop Duplicate Rows](https://leetcode.com/problems/drop-duplicate-rows/) | Introduction to Pandas | Completed | [View](01-introduction-to-pandas/2882-drop-duplicate-rows/solution.py) |
| 2883 | [Drop Missing Data](https://leetcode.com/problems/drop-missing-data/) | Introduction to Pandas | Completed | [View](01-introduction-to-pandas/2883-drop-missing-data/solution.py) |
| 2884 | [Modify Columns](https://leetcode.com/problems/modify-columns/) | Introduction to Pandas | Completed | [View](01-introduction-to-pandas/2884-modify-columns/solution.py) |
| 2885 | [Rename Columns](https://leetcode.com/problems/rename-columns/) | Introduction to Pandas | Completed | [View](01-introduction-to-pandas/2885-rename-columns/solution.py) |
| 2886 | [Change Data Type](https://leetcode.com/problems/change-data-type/) | Introduction to Pandas | Planned | [View](01-introduction-to-pandas/2886-change-data-type/solution.py) |
| 2887 | [Fill Missing Data](https://leetcode.com/problems/fill-missing-data/) | Introduction to Pandas | Planned | [View](01-introduction-to-pandas/2887-fill-missing-data/solution.py) |
| 2888 | [Reshape Data: Concatenate](https://leetcode.com/problems/reshape-data-concatenate/) | Introduction to Pandas | Planned | [View](01-introduction-to-pandas/2888-reshape-data-concatenate/solution.py) |
| 2889 | [Reshape Data: Pivot](https://leetcode.com/problems/reshape-data-pivot/) | Introduction to Pandas | Planned | [View](01-introduction-to-pandas/2889-reshape-data-pivot/solution.py) |
| 2890 | [Reshape Data: Melt](https://leetcode.com/problems/reshape-data-melt/) | Introduction to Pandas | Planned | [View](01-introduction-to-pandas/2890-reshape-data-melt/solution.py) |
| 2891 | [Method Chaining](https://leetcode.com/problems/method-chaining/) | Introduction to Pandas | Planned | [View](01-introduction-to-pandas/2891-method-chaining/solution.py) |

## Organization

Use this layout as new topics and exercises are added:

```text
pandas/
  README.md
  <topic-number>-<topic-name>/
    <problem-id>-<problem-name>/
      solution.py
```

For each exercise:

1. Add a directory and `solution.py` using the naming pattern above.
2. Start the solution with a docstring containing the problem title, `Algorithm:` describing the pandas operations, and time and space complexity.
3. Implement the required function and check it with example DataFrames and relevant edge cases.
4. Add a row to the exercise table and update its status when complete.

To run an implemented exercise with local example code, use its path from the repository root:

```sh
python pandas/01-introduction-to-pandas/2877-create-a-dataframe-from-list/solution.py
```

## Resources

- [LeetCode: Introduction to Pandas](https://leetcode.com/studyplan/introduction-to-pandas/)
- [Pandas documentation](https://pandas.pydata.org/docs/)
