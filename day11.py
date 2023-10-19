#eleventh commit
penghasilan_bulanan = 13000000
tagihan_rumah = 4000000
biaya_anak_pertama = 2000000
biaya_anak_lainnya = 1000000 * 2
maksimal_tabungan_per_bulan = 5000000
pengeluaran_bulanan_total = tagihan_rumah + biaya_anak_pertama + biaya_anak_lainnya
tabungan_per_bulan = penghasilan_bulanan - pengeluaran_bulanan_total
harga_pc_gaming = 150000000
bulan_yang_diperlukan = harga_pc_gaming / tabungan_per_bulan
tahun_yang_diperlukan = bulan_yang_diperlukan / 12
print("Total pengeluaran bulanan: ",pengeluaran_bulanan_total)
print("Total tabungan perbulan: ",tabungan_per_bulan)
print("Sambo perlu menabung selama",tahun_yang_diperlukan,"tahun untuk membeli PC gaming.")
