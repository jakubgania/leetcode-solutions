# https://leetcode.com/problems/method-chaining/

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    dataFrame = pd.DataFrame(animals)
    result = dataFrame[dataFrame['weight'] > 100].sort_values(by='weight', ascending=False)

    return result[['name']]