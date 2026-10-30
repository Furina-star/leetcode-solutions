"""
Create a New Column.
Algorithm: Multiply the salary column by 2 and assign it to the bonus column.
Time Complexity: O(n)
Space Complexity: O(n)
"""

import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees

def main():
    df = pd.DataFrame({
        "name": ["Piper", "Grace", "Georgia", "Willow", "Finn", "Thomas"],
        "salary": [4548, 28150, 1103, 65693, 74576, 24473],
    })

    result = createBonusColumn(df)
    print(result)

if __name__ == "__main__":
    main()
