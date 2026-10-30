"""
Drop Duplicate Rows
Algorithm: Hash-Based Duplicate Detection
Time Complexity: O(n)
Space Complexity: O(n)
"""

import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(
        subset=["email"],
        keep="first"
    )

def main():
    df = pd.DataFrame({
        "customer_id": [1, 2, 3, 4],
        "name": ["Piper", "Grace", "Georgia", "Willow"],
        "email": ["piper@gmail.com", "grace@gmail.com", "grace@gmail.com", "willow@gmail.com"],
    })

    result = dropDuplicateEmails(df)
    print(result)

if __name__ == "__main__":
    main()