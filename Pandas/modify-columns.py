# https://leetcode.com/problems/modify-columns/

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(employees)

    for index in df.index:
        df['salary'][index] = df['salary'][index] * 2

    return df