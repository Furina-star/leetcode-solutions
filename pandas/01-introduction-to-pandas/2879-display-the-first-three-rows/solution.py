"""
Display the First Three Rows.
Algorithm: Use employees.head(3) to return the first three rows of the DataFrame.
Time Complexity: O(1)
Space Complexity: O(1)
"""

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

def main():
    df = pd.DataFrame ({
        "employee_id": [3, 90, 9, 60, 49, 43],
        "name": ["Bob", "Alice", "Tatiana", "Annabelle", "Jonathan", "Khaled"],
        "department": ["Operations", "Sales", "Engineering", "InformationTechnology", "HumanRersources", "Administration"],
        "salary": [4875, 11096, 33805, 37678, 23793, 40454]
    })

    result = selectFirstRows(df)
    print(result)

if __name__ == "__main__":
    main()
