"""
Rename Columns
Algorithm: Dictionary-Based Column Renaming
Time Complexity: O(n)
Space Complexity: O(n)
"""

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={
        "id": "student_id",
        "first": "first_name",
        "last": "last_name",
        "age": "age_in_years",
    })

def main():
    df = pd.DataFrame({
        "id": [101, 53, 128, 3],
        "first": ["Ulysses", "William ", "Thomas", "Henry"],
        "last": ["King ", "Wright ", "Hall", "Thompson"],
        "age": [13, 10, 6, 11],
    })

    result = renameColumns(df)
    print(result)

if __name__ == "__main__":
    main()