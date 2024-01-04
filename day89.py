def hitung_gaji(jam_kerja, upah_per_jam):
  
  if jam_kerja <= 40:
    return jam_kerja * upah_per_jam
  else:
    return 40 * upah_per_jam + (jam_kerja - 40) * (upah_per_jam * 1.5)

jam_kerja = int(input("Masukkan jumlah jam kerja Anda: "))
upah_per_jam = int(input("Masukkan upah per jam Anda: "))
gaji = hitung_gaji(jam_kerja, upah_per_jam)
print("Gaji Anda adalah:", gaji)
