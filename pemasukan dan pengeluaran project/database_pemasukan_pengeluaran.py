import pandas as pd
import os

# Manggil data
if os.path.exists("data_login.xlsx"):
    df = pd.read_excel("data_login.xlsx")
    data = df.to_dict(orient="records")
else:
    data = []
# Manggil data saldo
if os.path.exists("saldo.xlsx"):
    df_saldo = pd.read_excel("saldo.xlsx")
    data_saldo = df_saldo.to_dict(orient="records")
else:
    data_saldo = []
# Manggil data tabungan sebenernya ga dipakee si
if os.path.exists("tabungan.xlsx"):
    df_tabungan = pd.read_excel("tabungan.xlsx")
    data_tabungan = df_tabungan.to_dict(orient="records")
else:
    data_tabungan = []