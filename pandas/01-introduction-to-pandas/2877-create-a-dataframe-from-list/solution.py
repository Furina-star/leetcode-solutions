"""
Create a DataFrame from List.
Algorithm: Use pandas.DataFrame constructor with the provided data and column names.
Time Complexity: O(n)
Space Complexity: O(n)
"""

import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=["student_id", "age"])
    return df

def main():
    student_data = [
        [1, 15],
        [2, 11],
        [3, 11],
        [4, 20]
    ]

    result = createDataframe(student_data)
    print(result)

if __name__ == "__main__":
    main()