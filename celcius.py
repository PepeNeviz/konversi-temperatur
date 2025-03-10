# Meminta pengguna memasukkan suhu dalam Celsius
celsius = float(input("Masukkan suhu dalam derajat Celsius: "))

# Mengonversi ke Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Menampilkan hasil
print(f"{celsius}°C sama dengan {fahrenheit:.2f}°F")
