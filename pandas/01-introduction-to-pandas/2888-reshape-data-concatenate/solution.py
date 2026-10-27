"""
Reshape Data: Concatenate
Algorithm: Vertical DataFrame Concatenation
Time Complexity: O(n+m)
Space Complexity: O(n+m)
"""

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    combined_df = pd.concat(
        [df1, df2],
        axis=0,
        ignore_index=True
    )

    return combined_df

def main():
    df1 = pd.DataFrame({
        "student_id": [101, 53],
        "name": ["Ulysses", "William "],
        "age": [13, 10],
    })

    df2 = pd.DataFrame({
        "student_id": [167, 169],
        "name": ["Furina", "Focalor "],
        "age": [500, 500],
    })

    result = concatenateTables(df1, df2)

    print(result)

if __name__ == "__main__":
    main()