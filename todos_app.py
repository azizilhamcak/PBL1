print("APLIKASI TO-DO LIST")

print("1. Tambahkan Tugas")
print("2. Lihat Tugas")
print("3. Hapus Tugas")
print("4. Keluar")

while True:
 try:
    user_input = int(input("Masukkan Pilihan : "))
    break
 except ValueError:
    print("Inputan harus berupa angka")
    
if user_input == 1:
    print("1. Tambahkan Tugas")
elif user_input == 2:
    print("2. Lihat Tugas")
elif user_input == 3:
    print("3. Hapus Tugas")
elif user_input == 4:
    print("4. Keluar")
else:
    print("Pilihan Tidak Ada")

nama = input("Masukkan Nama Anda : ")
tugas = []
def data():
    todo = input(f"Masukkan Tugas: ")
    while todo.lower() != "stop":
        tugas.append(todo) 
        todo = input(f"Masukkan Tugas: ")
def tampil():
    print(f"Selamat datang {nama}, ada memiliki beberapa kegiatan yaitu : {tugas}, tugas anda sebanyak : {len(tugas)}")

data()
tampil() 
exit_ = input("Apakah anda ingin keluar (y/n) : ")
if exit_ == 'y':
    print("Terima Kasih")
    exit()
else:
    print("Data akan di ulang")
    data()
    tampil()

   