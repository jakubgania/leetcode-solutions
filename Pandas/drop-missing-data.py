# https://leetcode.com/problems/drop-missing-data/

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(inplace=True)
    return students