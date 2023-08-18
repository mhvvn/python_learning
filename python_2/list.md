# List

## Menyusun Data
Mari belajar bagaimana mengelola sekelompok data dengan satu variable. Ketika ada daftar nama-nama makanan, sebagai contoh, tidak efisien untuk menamainya dengan variable terpisah, seperti food1, food2, food3. Akan lebih baik untuk mempunyai variable foods untuk mengelola keseluruhan daftar tersebut.
## List (Daftar)
Tipe data list memungkinkan Anda untuk mengelola sekelompok data sekaligus. Anda dapat membuat list sebagai berikut: [element1, element2, ...]. Setiap nilai di dalam list disebut element.
Dengan menggunakan list, Anda dapat mengelola banyak string dan integer dalam satu grup.

## Menetapkan List ke Variable

Seperti integer dan string, Anda dapat menentukan list ke dalam satu variable. Sesuai norma penamaan yang berlaku, nama variable bersifat plural, seperti foods, karena variable akan mengandung banyak element.

## Menentukan Element dalam List
Setiap element list dinomori 0, 1, 2, ....
Ini disebut nomor indeks. Nomor indeks dimulai dari 0. Anda bisa mendapatkan element individual dengan menulis list[index].



## Mari membuat list nama-nama buah!
- Buat list dengan string berikut sebagai element, dan tentukan ke variable fruits: apel, pisang, jeruk
- Petunjuk
Element harus dipisahkan dengan tanda koma ,. Contoh:
animals = ['anjing', 'kucing']
- Cetak element pada index 0.
- Sekarang, mari gunakan penggabungan string dengan sebuah element dari fruits.
- Dengan menggunakan element pada index 2, cetak 
Saya suka ___

```
# Tetapkan sebuah list string ke variable fruits
fruits = ['apel','pisang','jeruk']

# Cetak element di index 0
print (fruits[0])

# Gabungkan string dan element di index 2, dan cetak hasilnya

print ('Saya suka ' + fruits[2])
```
