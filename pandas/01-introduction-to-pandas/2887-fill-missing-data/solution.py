"""
Fill Missing Data
Algorithm:
Time Complexity: O(n)
Space Complexity: O(n)
"""

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products = products.fillna({"quantity":0})
    return products

def main():
    df = pd.DataFrame({
        "name": ["Ulysses", "William"],
        "quantity": [None, None],
        "price": [135, 821],
    })

    result = fillMissingValues(df)
    print(result)

if __name__ == "__main__":
    main()