print("APLIKASI TO-DO LIST")


tugas = []
nama = input("Masukkan Nama Anda : ")
while True:
    todo = input(f"Masukkan Tugas: ")
    tugas.append(todo) 
    if todo == "stop":
#jumlah = int(input("Masukkan Jumlah Tugas : "))
#for i in range(0, jumlah):
 #   todo = input(f"Masukkan Tugas: ")
  #  tugas.append(todo) ***  
        print(f"Selamat datang {nama}, ada memiliki beberapa kegiatan yaitu : {tugas}, tugas anda sebanyak : {len(tugas)}")
        exit_ = input("Apakah anda ingin keluar ? (y/n) : ")
        if exit_ == "y":
            print("Terimakasih")
            break
        else:
          print("Tambahkan tugas dan ketik stop jika ingin berhenti")
        