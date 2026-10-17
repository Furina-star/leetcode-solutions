"""
Get the Size of a DataFrame.
Algorithm: Convert players.shape to a list containing the row and column counts.
Time Complexity: O(1)
Space Complexity: O(1)
"""

import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

def main():
    df = pd.DataFrame({
        "player_id": [846, 749],
        "name": ["Mason", "Riley"],
        "age": [21, 30],
        "position": ["Forward", "Winger"],
        "team" :["Real Madrid", "Barcelona"]
    })

    result = getDataframeSize(df)

    print(result)

if __name__ == "__main__":
    main()
