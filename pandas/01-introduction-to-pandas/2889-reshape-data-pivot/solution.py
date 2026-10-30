
"""
Reshape Data: Pivot - Optimized Approach
Algorithm: DataFrame Pivoting (Long-to-Wide Reshaping)
Time Complexity: O(n log n + m*c)
Space Complexity: O(n + m*c)
"""

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(
        index="month",
        columns="city",
        values="temperature"
    )

def main():
    df = pd.DataFrame({
        "city": [
            "Jacksonville", "Jacksonville",
            "Jacksonville", "Jacksonville",
            "Jacksonville", "ElPaso",
            "ElPaso", "ElPaso", "ElPaso", "ElPaso"
        ],
        "month": [
            "January", "February", "March",
            "April", "May", "January",
            "February", "March", "April", "May"
        ],
        "temperature": [
            13, 23, 38, 5, 34,
            20, 6, 26, 2, 43
        ]
    })

    result = pivotTable(df)
    print(result)

if __name__ == "__main__":
    main()
