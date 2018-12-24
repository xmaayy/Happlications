import pandas as pd
import numpy as np
import pdb


def hist(
    vals: list,
    disp: bool = False,
    trimp: float = 0.05,
    xlab="Num",
    ylab="Ciel",
    label: str = "Question:",
):
    """
    Makes a histogram. Finds the 'optimal' number of bins with the 
    Freedman-Diaconis method, and returns the percentage of data
    falling into each of the bins

    bin width = 2 * IQR * n^(-1/3)

    params vals: A list of integers
    """
    # Trimming the top bit
    vals.sort()
    ml = len(vals) - int(trimp * len(vals)) - 1
    vals = vals[:ml]

    # Getting IQR
    spltvals = len(vals) // 2
    offset = spltvals // 2
    Q1 = vals[offset]
    Q3 = vals[spltvals + offset]
    IQR = Q3 - Q1

    # Bin width h
    h = 2 * IQR * (len(vals) ** (-1 / 3))

    # N bins
    n = int((max(vals) - min(vals)) // h)

    # get his vals
    sumlist = []
    uppers = []

    for binn in range(n):
        lower = (binn * h) + min(vals)
        upper = ((binn + 1) * h) + min(vals)
        sumlist.append(len([el for el in vals if lower <= el < upper]))
        uppers.append(upper)
    if disp:
        print(label)
        print("Total Datapoints:" + str(sum(sumlist)))
        print("{0}\t {1}".format(xlab, ylab))
        for ind, el in enumerate(sumlist):
            print("{0}\t {1}".format(el, round(uppers[ind])))

    return sumlist, uppers


def norm_col(col: np.ndarray, trimp: float = 0.05, axis=0):
    """
    Normalize a column to give a relative ranking. Each category will
    have people who overperform for sure, so I try to remove them with
    a 5% trim on the max
    """

    if not isinstance(col, np.ndarray):
        raise RuntimeError("Col type error")

    # Grad the element that is at the last `trimp`% of the data
    # to use as the denominator. Normalize any elements above 1 to 1
    numel = col.shape[axis]
    ml = numel - int(trimp * numel) - 1
    denom = np.sort(col)[ml]
    col = [el / denom for el in col]
    col = [1 if el > 1 else el for el in col]

    return col


def normalize(
    data: pd.DataFrame, col: str = None, sort: str = None, perc: float = 0.05
):
    if type(data) != pd.DataFrame:
        raise RuntimeError("Data must be in a dataframe")

    if col is None and sort is None:
        raise RuntimeError("You have to give me one of the two: col/sort")

    # If you specify a single column to process
    if col is not None and col in data and data[col].dtype != str:
        data[col] = norm_col(data[col].values)
    elif col == 'all':
        # The columns we should be processing are only the numerical ones
        # here we filter out the non numerical columns

        cols = [
            col for col in data.columns.values if data[col].dtype != object
        ]
        for col in cols:
            data[col] = norm_col(data[col].values)
    if sort:
        data = data.sort_values(by=[sort])
    return data
