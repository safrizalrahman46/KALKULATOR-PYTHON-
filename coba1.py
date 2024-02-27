# Pocedure  menu()
def menu():
    print("Kalkulator Bermenu")
    print("1.  Penambahan")
    print("2.  Pengurangan")
    print("3.  Perkalian")
    print("4.  Pembagian")
    print("5.  Tamat")

# Function dptPilihanPengguna()
def dptPilihanPengguna():
    noPilihan = 0
    while (noPilihan < 1) or (noPilihan > 5):
      noPilihan = int(input("Pilih nomor [1 hingga 5] :   "))
    return noPilihan
    
# Function dptDuaNombor()
def dptDuaNombor():
    nombor1 = int(input("Masukkan Angka Pertama :   "))
    nombor2 = int(input("Masukkan Angka Kedua:   "))
    return nombor1, nombor2

# Procedure kiraCetak()
def kiraCetak(jenisOperator, a, b):
    if jenisOperator == 1:
       print("Output: " + str(a) + "+" + str(b) + "=" + str(a + b) + "\n")
    elif jenisOperator == 2:
       print("Output: " + str(a) + "-" + str(b) + "=" + str(a - b) + "\n")
    elif jenisOperator == 3:
       print("Output: " + str(a) + "*" + str(b) + "=" + str(a * b) + "\n")
    elif jenisOperator == 4:
       print("Output: " + str(a) + "/" + str(b) + "=" + str(a / b) + "\n")
       
# main -------------------------------------------------------------------------------
aktif = 1
while aktif == 1:
    menu()
    jenisOperasi = dptPilihanPengguna()
    if jenisOperasi == 5:
       aktif = 0
    else:
       [nom1, nom2] = dptDuaNombor()
       kiraCetak(jenisOperasi, nom1, nom2)
print("Terima kasih kerana menggunakan saya.")
#---------------------------------------------------------------------------------------




# print('=' * 25)
# print('Operasi Matematika')
# print('  1. Jumlah \t [+]')
# print('  2. Kurang \t [-]')
# print('  3. Kali \t [*]')
# print('  4. Bagi \t [/]')
# print('=' * 25)

# operasi = input('Pilih operasi (1/2/3/4): ')
# bilangan_1 = eval(input('Masukkan bilangan pertama: '))
# bilangan_2 = eval(input('Masukkan bilangan kedua: '))

    # thisdict_1 = {
    # "brand": "Ford",
    # "electric": False,
    # "year": 1964,
    # "colors": ["red", "white", "blue"]
    # }

    # operasi ={
    #     aaa = aaa,
    # }
    # print('=' * 25)

    # if operasi == '1':
    # print('User memilih penjumlahan')
    # elif operasi == '2':
    # print('User memilih pengurangan')
    # elif operasi == '3':
    # print('User memilih perkalian')
    # elif operasi == '4':
    # print('User memilih pembagian')
    # else:
    # print('Tidak valid')