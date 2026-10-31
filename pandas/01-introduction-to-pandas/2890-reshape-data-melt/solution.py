"""
Reshape Data: Melt - Optimized Approach
Algorithm: Wide-to-Long DataFrame Reshaping
Time Complexity: O(n)
Space Complexity: O(n)
"""

import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report = report.melt(id_vars=["product"], var_name="quarter", value_name="sales")

    return report


def main():
    df = pd.DataFrame(
        {
            "product": ["Umbrella", "SleepingBag"],
            "quarter_1": [417, 800],
            "quarter_2": [224, 936],
            "quarter_3": [379, 93],
            "quarter_4": [611, 875],
        }
    )

    result = meltTable(df)
    print(result)


if __name__ == "__main__":
    main()
