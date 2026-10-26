"""
Change Data Type
Algorithm: Vectorized Data Type Conversion
Time Complexity: O(n)
Space Complexity: O(n)
"""

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students

def main():
    df = pd.DataFrame({
        "student_id": [101, 53],
        "name": ["Ulysses", "William "],
        "age": [13, 10],
        "grade": [73.0, 87.0],
    })

    result = changeDatatype(df)
    print(result)

if __name__ == "__main__":
    main()