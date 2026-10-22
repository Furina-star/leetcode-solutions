"""
Drop Missing Data
Algorithm: Null-Value Removal
Time Complexity: O(n)
Space Complexity: O(n)
"""

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])

def main():
    df = pd.DataFrame({
        "student_id": [32, 217, 779, 849],
        "name": ["Piper", None, "Georgia", "Willow"],
        "age": [5, 19, 20, 14],
    })

    result = dropMissingData(df)
    print(result)

if __name__ == "__main__":
    main()