import pandas as pd
from database_pemasukan_pengeluaran import data, data_saldo, data_tabungan

def bikin_akun():
   print("DAFTAR AKUN BARU")
   buat_akun = input("Masukan ID anda: ")
   pass_akun = input("Masukan Password anda: ")
   print("Akun anda berhasil dibuat!")
   # menambah ke database
   data.append({"ID":buat_akun,"PASSWORD":pass_akun})
   df = pd.DataFrame(data)
   df.to_excel("data_login.xlsx", index=False)

def login():
   print("Selamat datang")
   id_akun = input("Masukan ID anda: ")
   password_akun = input("Masukan PASSWORD anda: ")
   # ngecek akun yang ada di database
   for akun in data:
      if akun["ID"] == id_akun and akun["PASSWORD"] == password_akun:
         return id_akun
   print("ID atau PASSWORD anda salah / tidak ada!")
   return False

def tabungan(id_user):
   # untuk sementara sebelum masuk ke data tabungan
   tabungan_user = []
   print("Tabungan anda")
   while True:
      try:
         uang_tabungan = int(input("Masukan jumlah yang ingin anda tabung: "))
         tanggal = input("Masukan tanggal yyyy-mm-dd: ")
         tabungan_user.append({
            "ID": id_user,
            "Tabungan": uang_tabungan,
            "Tanggal": tanggal,
         })
         print(f"Selamat anda telah menabung sebesar{uang_tabungan}")
      except ValueError:
         print("Eror: Masukan angka yang valid!")
         continue
      total = sum(item["Tabungan"] for item in tabungan_user)
      keluar = input("Apakah anda ingin menabung lagi?(Y/N): ")
      if keluar == "N" or keluar == "n":
         break
   # Menjadi satu data ke data saldo 
   try:
      df_saldo = pd.read_excel("saldo.xlsx")
      df_tabungan = pd.DataFrame(tabungan_user)
      df_gabung = pd.concat([df_saldo, df_tabungan], ignore_index=True)
   except FileNotFoundError:
      df_gabung = pd.DataFrame(tabungan_user)
   df_gabung.to_excel("saldo.xlsx", index=False)

def pemasukan(id_user):
    pemasukan_user = []
    while True:
       try:
         pemasukan = int(input("Masukan saldo pemasukan anda: "))
         tanggal = input("Masukan tanngal (yyyy-mm-dd): ")
         pemasukan_user.append({
            "ID": id_user,
            "Uang Masuk": pemasukan,
            "Tanggal": tanggal
            })
         print(f"Berhasil memasukan saldo anda sebesar {pemasukan_user}")
       except ValueError:
          print("Eror: Masukan angka yang valid!")
          continue
       total = sum(item["Uang Masuk"] for item in pemasukan_user)
       print(f"Total saldo anda sekarang: Rp{total}")
       keluar = input("Apakah anda ingin memasukan saldo lagi?(Y/N): ")
       if keluar == "N" or keluar == "n":
          break
      # Masuk ke data saldo dari list sementara
    data_saldo.extend(pemasukan_user)

    df = pd.DataFrame(data_saldo)
    df.to_excel("saldo.xlsx", index=False)

def pengeluaran(id_user):
   pengeluaran_user = []
   while True:
      try:
         pengeluaran = int(input("Masukan pengeluaran anda: "))
         tanggal = input("Masukan tanggal pengeluaran (yyyy-mm-dd): ")
         reason = input("Pengeluaran untuk apa?: ")
         pengeluaran_user.append({
            "ID": id_user,
            "Uang Keluar": pengeluaran,
            "Tanggal": tanggal,
            "Reason": reason
         })
         print(f"Berhasil, pengeluaran anda pada {tanggal} sebanyak: Rp{pengeluaran}")
      except ValueError:
         print("Eror: Masukan angka yang valid!")
         continue
      total = sum(item["Uang Keluar"] for item in pengeluaran_user)
      keluar = input("Apakah ada pengeluaran lagi?(Y/N): ")
      if keluar == "N" or keluar == "n":
         break
      # Masuk ke data saldo dari list sementara
   data_saldo.extend(pengeluaran_user)

   df = pd.DataFrame(data_saldo)
   df.to_excel("saldo.xlsx", index=False)

def cek_saldo(id_user):
   import pandas as pd
   df = pd.read_excel("saldo.xlsx")
   # Mengecek columns yang ada di excel saldo
   if "Uang Masuk" not in df.columns:
      df["Uang Masuk"] = 0
   if "Uang Keluar" not in df.columns:
      df["Uang Keluar"] = 0
   if "Tabungan" not in df.columns:
      df["Tabungan"] = 0
   # Pemanggilan dari data saldo
   df_user = df[df["ID"] == id_user]
   total_masuk = df_user["Uang Masuk"].sum()
   total_keluar = df_user["Uang Keluar"].sum()
   total_tabungan = df_user["Tabungan"].sum()
   total = total_masuk - total_keluar - total_tabungan
   print(f"Total saldo {id_user}: Rp{total}")

def cek_tabungan(id_user):
   df = pd.read_excel("saldo.xlsx")
   df_user = df[df["ID"] == id_user]
   cek_tabungan_user = df_user["Tabungan"].sum()
   print(f"Tabungan anda sekarang Rp{cek_tabungan_user}")

def history(id_user):
   print("History anda!")
   df = pd.read_excel("saldo.xlsx")
   df_user = df[df["ID"] == id_user]

   masuk = df_user[["Tanggal", "Uang Masuk"]].dropna(subset=["Uang Masuk"]).reset_index(drop=True)
   tabungan = df_user[["Tanggal", "Tabungan"]].dropna(subset=["Tabungan"]).reset_index(drop=True)
   keluar = df_user[["Tanggal", "Uang Keluar", "Reason"]].dropna(subset=["Uang Keluar"]).reset_index(drop=True)

   history_transaksi = pd.concat([masuk, keluar, tabungan], ignore_index=True)
   history_transaksi = history_transaksi.fillna("-")
   print(history_transaksi.to_string(index=False))
