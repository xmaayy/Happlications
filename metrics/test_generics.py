from generic_fns import *
import pandas as pd


def test_norm():
    cols = ["hello", "darkness", "num1", "num2"]
    df = pd.DataFrame(columns=cols)
    df["hello"] = ["hello", "darlness", "my", "OLD", "friend"]
    df["testing"] = [
        ["l", "a", "d"],
        ["l", "a", "d"],
        ["l", "a", "d"],
        ["l", "a", "d"],
        ["l", "a", "d"],
    ]
    df["darkness"] = ["hello", "darlness", "my", "OLD", "friend"]
    df["num1"] = [1, 5, 3, 4, 2]
    df["num2"] = [5.1, 6.1, 7.1, 8.1, 9.1]
    print("")
    print(df.head())
    print(normalize(df, sort="num1").head())
