import numpy as np
import os.path
import datetime as dt
import pandas as pd


def df_load_stooq_data(str_data_file_path: str, str_ts_name: str):
    df = pd.read_csv(str_data_file_path)
    df["Date"] = df["Date"].apply(lambda x: dt.datetime.strptime(x, "%Y-%m-%d").date())
    l_str_non_date_cols = list(set(df.columns).difference({"Date"}))
    for col in l_str_non_date_cols:
        df[col] = df[col].astype(np.float32)
    dict_renaming = dict(zip(l_str_non_date_cols, [(str_ts_name + "_" + el).lower() for el in l_str_non_date_cols]))
    dict_renaming.update({"Date": "date"})
    df.rename(columns=dict_renaming, inplace=True)
    df = df.loc[df["date"] >= dt.date(1995, 1, 1), :]
    df.reset_index(inplace=True, drop=True)
    return df


def df_load_us_yield_curve_data() -> pd.DataFrame:
    str_data_file_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "data", "yield-curve-rates-1990-2021.csv")
    df = pd.read_csv(str_data_file_path)
    df.columns = l_str_format_headers(list(df.columns))
    df["date"] = df["date"].apply(lambda x: dt.datetime.strptime(x, "%m/%d/%y").date())
    df.sort_values("date", ascending=True, inplace=True)
    df.reset_index(inplace=True, drop=True)
    df = df[["date", "3_mo", "2_yr", "10_yr"]]
    df = df.loc[df["date"] >= dt.date(1995, 1, 1), :]
    df.rename(columns={"3_mo": "usyc_3m", "2_yr": "usyc_2y", "10_yr": "usyc_10y"}, inplace=True)
    df.reset_index(inplace=True, drop=True)
    return df


def df_process_us_yield_curve_data(df: pd.DataFrame):
    # calculate rates' changes
    l_str_val_cols = list(set(df.columns).difference({"date"}))
    df[l_str_val_cols] = df[l_str_val_cols].diff(periods=1)
    df.rename(columns=dict(zip(l_str_val_cols, ["delta_" + el for el in l_str_val_cols])), inplace=True)
    return df


def l_str_format_headers(l_str_headers: list[str]):
    return [el.replace(" ", "_").lower() for el in l_str_headers]


def df_prepare_wig20_data():
    pass


def df_prepare_usdpln_data():
    pass


def df_prepare_spx_data():
    pass