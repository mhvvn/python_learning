# Mari belajar cara menggabungkan conditional expression!

# AND
# Anda dapat menggunakan operator and untuk menggabungkan kondisi. 
# bagai contoh, Kondisi1 and Kondisi2 akan menampilkan True ketika kedua kondisi terpenuhi.

# OR
# Anda dapat menggunakan operator or pada cara yang sama. Kondisi1 or Kondisi2 akan menampilkan True jika salah satu Kondisi1 atau Kondisi2 benar.
# ini berarti kondisi gabungan akan menampilkan True jika setidaknya satu conditional expression True.

# NOT
# Dengan menggunakan not, Anda dapat menegasikan suatu kondisi.
# Ini artinya False akan muncul jika conditional expression benar dan True akan muncul jika salah.

#merantai perbandingan operator
#Anda dapat menulis ulang kondisi and yang menggunakan variable yang sama dengan cara 
#yang ditunjukkan gambar di bawah!  Hal ini disebut merantai perbandingan operator.

x = 20
# Jika x berkisar antara 10 dan 30 (inklusif), cetak 'x berkisar antara 10 dan 30'
if x >= 10 and x <= 30 :
  print ('x berkisar antara 10 dan 30')


y = 60
# Jika y lebih kecil dari 10 atau lebih besar dari 30, cetak 'y lebih kecil dari 10 atau lebih besar dari 30'
if y < 10 or y > 30 :
  print('y lebih kecil dari 10 atau lebih besar dari 30')


z = 55
# Jika z tidak sama dengan 77, print 'z bukan 77'
if not z == 77 :
  print('z bukan 77')


