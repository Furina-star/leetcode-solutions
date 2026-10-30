"""
Select Data.
Algorithm: Boolean Filtering and Column Selection with .loc
Time Complexity: O(n)
Space Complexity: O(n)
"""

import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]

def main():
    df = pd.DataFrame({
        "student_id": [101, 53, 128, 3],
        "name": ["Ulysses ", "William ", "Henry", "Henry"],
        "age": [13, 10, 6, 11],
    })

    result = selectData(df)
    print(result)

if __name__ == "__main__":
    main()
