import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display as dp
import re
import duckdb
from collections import Counter
from termcolor import cprint
import seaborn as sns
import sqlite3

import matplotlib.ticker as ticker
from statsmodels.graphics.mosaicplot import mosaic
import os
from scipy.stats import binomtest


# plotting related
def s():
    """
    Lazy function for plt.show()
    """
    plt.show()


def fs(w=3, h=3):
    """
    Lazy function for setting figure size

    Args:
        w (int, optional): set fig width. Defaults to 3.
        h (int, optional): set fig length. Defaults to 3.
    """
    plt.figure(figsize=(w, h))


def bprint(input):
    """
    Style printing

    Args:
        input (any): content to print
    """
    cprint(f"\n{input}", "green", attrs=["bold"])


def mark_bar(plot):
    """
    Append bar values on the bars

    Args:
        plot (matplotlib axis): plot
    """
    for i in plot.containers:
        plot.bar_label(
            i,
        )


def qry(query):
    """
    Wrapper function for running duckdb query, and convert result to pandas dataframe

    Args:
        query (str): sql query

    Returns:
        query result: query result in pandas dataframe
    """
    return duckdb.sql(query).to_df()


def find_list_pattern(regex_term, ls):
    """
    Search in a list to find elements with certain pattern

    Args:
        regex_term (string): pattern to match
        ls (list): a list to search in

    Returns:
        list: list of items with matching pattern
    """
    reg = re.compile(regex_term)
    result = [i for i in ls if reg.match(i)]
    return result


def drop_cols(df, cols):
    """
    Drop certain columns in a df after checking that the columns exists.
    Args:
        df : dataframe to drop columns
        cols: columns to drop

    Returns:
        df: columns dropped dataframe
    """
    if len(cols) == 0:
        return df
    elif cols[0] in df.columns:
        df = df.drop(columns=cols)
        return df
    else:
        return df


def merge_df(left_df, right_df, on="col", how="left"):
    """
    merge dataframes after checking that the right_df has columns that is not in the left_df

    Args:
        left_df (_type_): _description_
        right_df (_type_): _description_
        on (str, optional): _description_. Defaults to "col".
        how (str, optional): _description_. Defaults to "left".

    Returns:
        df: merged df.
    """
    new_cols = list(right_df.columns)
    new_cols.remove(on)
    if new_cols[0] in left_df.columns:
        return left_df
    else:
        return pd.merge(left_df, right_df, on=on, how=how)


def camel_to_slug(input_str):
    """
    Replace capital letters with hyphen followed by lowercase letter

    Args:
        input_str (_type_): _description_

    Returns:
        _type_: _description_
    """
    slug_case = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", input_str)
    slug_case = slug_case.lower()
    return slug_case


def basic_df_info(df, head=True):
    """
    display null, duplication count, datashape, and the head of df

    Args:
        df : dataframe to display
        head (bool, optional): show df head. Defaults to True.
    """
    bprint("null count:")
    print(df.isnull().sum().sum())
    bprint("duplication count:")
    print(df.duplicated().sum())
    bprint("data shape:")
    print(df.shape)
    bprint("df:")
    if head:
        dp(df.head(3))
    else:
        dp(df)
