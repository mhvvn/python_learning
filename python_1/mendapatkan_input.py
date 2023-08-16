# input() 
# memungkinkan Anda dapat mengisi angka pada console ketika menjalankan code, dan menerima nilai yang dimasukkan.
# Dengan menulis variable = input('string yang ingin Anda tampilkan di console')
# nilai akan ditentukan ke variable.


#  Tipe Konversi Nilai Input
# Nilai yang Anda dapatkan dari input() adalah string, 
# bahkan jika Anda mengisinya dengan angka. 
# Jika Anda ingin menggunakan nilainya sebagai integer untuk sebuah perhitungan,
# Anda harus mengonversinya ke tipe data integer, seperti gambar di bawah.

apple_price = 2

# Terima jumlah apel dengan menggunakan input(), dan berikan hasilnya ke variable input_count 
input_count = input('Mau berapa apel?: ') 

# Ubah variable input_count ke integer, dan berikan hasilnya ke variable count 
count = int(input_count)
total_price = apple_price * count

print('Anda akan membeli ' + str(count) + ' apel')
print('Harga total adalah ' + str(total_price) + ' dolar')