# Anda dapat menggunakan elif untuk menambah kondisi alternatif pada control flow
# Anda dapat menambah elif sebanyak yang Anda inginkan.
# Akan tetapi, hanya code pada kondisi pertama yang dipenuhi yang akan dijalankan.

money = 2
apple_price = 2

if money > apple_price:
    print('Anda dapat membeli apel')
# Ketika kedua variable memiliki nilai yang sama, cetak 'Anda dapat membeli apel tetapi dompet Anda akan menjadi kosong'
elif money == apple_price :
  print ('Anda dapat membeli apel tetapi dompet Anda akan menjadi kosong')
else:
    print('Uang Anda tidak mencukupi')
