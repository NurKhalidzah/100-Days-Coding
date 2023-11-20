no_atm = int(input("No ATM: "))
password = int(input("Pass: "))
if no_atm == 12345 and password == 321:
	print("Login Sukses")
	print("***************************")
	print("1. Cek Saldo")
	print("2. Transfer")
	pilihan = int(input("Masukkan Pilihan: "))
	if pilihan == 1:
		print("Saldo anda 0")
	elif pilihan == 2:
		atm_tujuan = int(input("No ATM yang di tuju: "))
		if atm_tujuan == 6789:
				print("Transfer Berhasil")
		else:
			print("Transfer Gagal")
else:
	print("Login Gagal")