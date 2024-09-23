print("APLIKASI TO-DO LIST")


nama = input("Masukkan Nama Anda : ")
jumlah = int(input("Masukkan Jumlah Tugas : "))
tugas = []

for i in range(0, jumlah):
    todo = input(f"Masukkan Tugas: ")
    tugas.append(todo)
    
print(f"Selamat datang {nama}, ada memiliki beberapa kegiatan yaitu : {tugas}, tugas anda sebanyak : {len(tugas)}")
exit_ = input("Apakah anda ingin keluar ? (y/n) : ")
if exit_ == "y":
    print("Terimakasih")
else:
    print("Program akan diulang")
    exit()
    