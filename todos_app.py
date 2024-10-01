print("APLIKASI TO-DO LIST")

def name():
    nama = input("Masukkan Nama Depan : ")
    nama1 = input("Masukkan Nama Belakang : ")
    return f"{nama} {nama1}"

def tampilnama(fullname):
    print(f"Selamat Datang {fullname}")

    
def menu():
    print("1. Tambahkan Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

def user_input_cek():
    while True:
     try:
          user_input = int(input("Masukkan Pilihan : "))
          if user_input in [1,2,3,4]:
             return user_input
          else:
             print("Pilihan Tidak Tersedia")
     except ValueError:
           print("Inputan harus berupa angka")
def user_menu(user_input):
    if user_input == 1:
        print("1. Tambahkan Tugas")
        data()
    elif user_input == 2:
        print("2. Lihat Tugas")
        print("Masukkan tugas anda terlebih dahulu")
        try:
            if user_input == 2:
                return data()
        except NameError:
            print("Masukkan tugas anda terlebih dahulu")           
        tampil()
    elif user_input == 3:
        print("3. Hapus Tugas")
    elif user_input == 4:
        print("4. Keluar")
        keluar()
def data():
    todo = input(f"Masukkan Tugas: ")
    global tugas
    tugas = []
    while todo.lower() != "stop":
        tugas.append(todo)
        todo = input(f"Masukkan Tugas: ")
    return menu(), user_input_cek(), tampil()

def tampil():
        print(f"Selamat Datang {fullname}, tugas Anda adalah:")
        num = 1 
        for i in tugas:
            print(f"{num}.{i}")
            num += 1
        print(f"Jumlah, tugas anda sebanyak : {len(tugas)}")
def keluar():    
    exit_ = input("Apakah anda ingin keluar (y/n) : ")
    if exit_ == 'y':
        print("Terima Kasih")
        exit()
    else:
        print("Silahkan tambahkan tugas anda: ")
        data()
        tampil()

fullname = name()
tampilnama(fullname)
menu()
user_input = user_input_cek()
user_menu(user_input)