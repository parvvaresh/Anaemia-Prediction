import pandas as pd
from standardize import standardize

def pre_process(df: pd.DataFrame, class_column: str) -> list:
    print("📌 Start pre process ...")

    # Renaming columns
    cols_to_rename = {'%Red Pixel': 'red_pixel',
                      '%Green pixel': 'green_pixel',
                      '%Blue pixel': 'blue_pixel'}

    df.rename(columns=cols_to_rename, inplace=True)
    df.columns = map(str.lower, df.columns)

    # Removing column which do not need in the dataset
    df.drop("number", axis=1, inplace=True)

    # Standardising the values in the sex category (keeping 'M' and 'F')
    df['sex'] = df['sex'].replace(['M ', 'F '], ["M", "F"])

    df['sex'] = df['sex'].replace({'M': 0, 'F': 1})

    X, y = df.drop(class_column.lower(), axis=1), df[class_column.lower()]

    # Apply standardization on the features
    standardize_data = standardize(X)
    print("--- ✅finish pre process ...")

    return standardize_data, y
