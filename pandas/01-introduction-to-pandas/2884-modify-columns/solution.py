"""
Modify Columns
Algorithm: Vectorized Column Transformation
Time Complexity: O(n)
Space Complexity: O(n)
"""

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"] * 2
    return employees

def main():
    df = pd.DataFrame({
        "name": ["Jack", "Piper", "Mia", "Ulysses"],
        "salary": [39332, 149508, 125018, 109732],
    })

    result = modifySalaryColumn(df)
    print(result)

if __name__ == "__main__":
    main()