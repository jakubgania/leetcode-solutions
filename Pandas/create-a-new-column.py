# https://leetcode.com/problems/create-a-new-column/

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    bounus_arr = []
    df = pd.DataFrame(employees)

    for index in df.index:
        bounus_arr.append(df['salary'][index] * 2)

    df['bonus'] = bounus_arr

    return df