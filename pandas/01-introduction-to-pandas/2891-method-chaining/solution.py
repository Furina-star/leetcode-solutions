"""
Method Chaining
Algorithm: Filter, Sort, and Select (Method Chaining)
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals.loc[animals["weight"] > 100].sort_values("weight", ascending=False)[
        ["name"]
    ]


def main():
    df = pd.DataFrame(
        {
            "name": ["Tatiana", "Khaled", "Alex", "Jonathan", "Stefan", "Tommy"],
            "species": ["Snake", "Giraffe", "Leopard", "Monkey", "Bear", "Panda"],
            "age": [98, 50, 6, 45, 100, 26],
            "weight": [464, 41, 328, 463, 50, 349],
        }
    )

    result = findHeavyAnimals(df)
    print(result)


if __name__ == "__main__":
    main()
