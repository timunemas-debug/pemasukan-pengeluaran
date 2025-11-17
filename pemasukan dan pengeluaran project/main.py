from pemasukan_pengeluaran import bikin_akun, login, pemasukan, cek_saldo,pengeluaran,history,tabungan,cek_tabungan

while True:
 print("=====================================")
 print("      Pemasukan dan Pengeluaran      ")
 print("=====================================")
 print("    1.Login                          ")
 print("    2.Buat akun                      ")
 print("    3.Keluar                         ")
 print("=====================================")
 login_sistem = input("Masukan pilihan anda: ")
 if login_sistem == "1":
   id_user = login()
   if id_user:
     print(f"Selamat datang {id_user}")
   else:
     print("Login Gagal!")
     exit()
 elif login_sistem == "2":
   bikin_akun()
   login()
 else:
   break
 while True:
   print("=======PENGELUARAN&PEMASUKAN=======")
   print("1.Catatan Pemasukan   2.Catatan pengeluaran")
   print("3.Tabungan            4.Cek Saldo")
   print("5.History             6.Log Out Account")
   print("===================================")
   input_user = input("Masukan angka yang ingin anda pilih: ")
   if input_user == "1":
     pemasukan(id_user)
   elif input_user == "2":
     pengeluaran(id_user)
   elif input_user == "3":
     print("1.Cek tabungan")
     print("2.Menabung")
     rsp_user = input("Masukan pilihan anda: ")
     if rsp_user == "2":
      tabungan(id_user)
     else:
       cek_tabungan(id_user)
   elif input_user == "4":
     cek_saldo(id_user)
   elif input_user == "5":
     history(id_user)
   else:
     break
   keluar = input("Apakah anda ingin log out?(Y?N): ")
   if keluar == "Y" or keluar == "y":
     id_user = login()
