import numpy as np
import os
import pandas as pd
from wig20_ann_modeling.utils.utils import df_load_stooq_data, df_load_us_yield_curve_data, \
    df_process_us_yield_curve_data

str_data_file_path = os.path.join(
    '/Users/arturwegrzyn/github_repos/wig20_ann_modeling', "wig20_ann_modeling", "data", "wig20_d.csv"
)
str_ts_name = "wig20"
df_wig20 = df_load_stooq_data(str_data_file_path=str_data_file_path, str_ts_name=str_ts_name)
df_wig20.columns

# calculate DtD log-return of close price
df_wig20["logret_wig20_close"] = np.log(df_wig20["wig20_close"] / df_wig20["wig20_close"].shift(1))
df_tom_next = df_wig20[["date", "wig20_close"]].copy()
df_tom_next = df_tom_next.assign(**{
    "lead1_wig20_close": df_tom_next["wig20_close"].shift(-1),
    "lead2_wig20_close": df_tom_next["wig20_close"].shift(-2)
})
df_tom_next["logret_wig20_tom_next"] = np.log(df_tom_next["lead2_wig20_close"] / df_tom_next["lead1_wig20_close"])
df_tom_next["binary_wig20_tom_next"] = np.where(df_tom_next["logret_wig20_tom_next"] > 0, 1, -1)
df_tom_next = df_tom_next[["date", "logret_wig20_tom_next", "binary_wig20_tom_next"]]
df_wig20 = pd.merge(left=df_wig20, right=df_tom_next, on="date", how="left")
df_wig20


# df_us_yc = df_load_us_yield_curve_data()
# df_us_yc = df_process_us_yield_curve_data(df=df_us_yc)
# class AnnData:
#
#     def __init__(self):
#         self.str_data_folder_path = os.path.join(
#             os.path.dirname(__file__),
#         )
#
#     def load_dataset(self):
#         # 1. load stooq data
#         dict_of_stooq_data = {
#             "sp500": "^spx_d.csv", "usd_index": "usd_i_d.csv", "usdpln": "usdpln_d.csv", "wig20": "wig20_d.csv"
#         }
#
#         # 2. load US YC data
#         # 3. merge the datasets
#
#         pass