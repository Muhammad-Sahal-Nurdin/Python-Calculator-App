
import math

input1 = eval(input("Masukkan angka pertama: "))
input2 = eval(input("Masukkan angka kedua: "))

print("Menu Kalkulator")
print("Pilihlah menu berikut.")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Pembagian")
print("4. Perkalian")
print("5. Modulo")
print("6. Perpangkatan")
print("7. Akar")
print("8. Keluar")

while True:
    pilihan = int(input("Masukkan pilihan nomor 1/2/3/4/5/6/7/8: "))
    if pilihan in (1, 2, 3, 4, 5, 6, 7, 8):
        if pilihan == 1:
            print("Hasil dari penjumlahan kedua bilangan tersebut adalah ", input1 + input2)
        elif pilihan == 2:
            print("Hasil dari pengurangan kedua bilangan tersebut adalah ", input1 - input2)
        elif pilihan == 3:
            print("Hasil dari pembagian kedua bilangan tersebut adalah ", input1 / input2)
        elif pilihan == 4:
            print("Hasil dari perkalian kedua bilangan tersebut adalah ", input1 * input2)
        elif pilihan == 5:
            print("Hasil dari modulo kedua bilangan tersebut adalah ", input1 % input2)
        elif pilihan == 6:
            input3 = eval(input("Masukkan pangkat yang mau dicari dari kedua bilangan: "))
            print("Hasil dari perpangkatan kedua bilangan 1 adalah ", input1 ** input3)
            print("Hasil dari perpangkatan kedua bilangan 2 adalah ", input2 ** input3)
        elif pilihan == 7:
            print("Hasil dari akar kedua bilangan 1 adalah ", math.sqrt(input1))
            print("Hasil dari akar kedua bilangan 2 adalah ", math.sqrt(input2))
        elif pilihan == 8:
            print("Terima kasih :)")
            exit()
    else:
        print("Maaf pilihan yang Anda input tidak ada dalam sistem, Mohon coba kembali")
