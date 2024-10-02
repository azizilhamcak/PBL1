print("APLIKASI TO-DO LIST")

user_input = int
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
def user_menu():
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
        user_input_cek()
    elif user_input == 3:
        hapus()
        user_input_cek()
    elif user_input == 4:
        keluar()
        print("4. Apakah Anda yakin akan keluar ?")


def data():
    todo = input(f"Masukkan Tugas: ")
    global tugas
    tugas = []
    while todo.lower() != "stop":
        tugas.append(todo)
        todo = input(f"Masukkan Tugas: ")
    return user_input_cek()

def hapus():
    tugas_hapus = int(input("Hapus Tugas ke : ")) - 1
    tugas.pop(tugas_hapus)
    return user_input_cek()

def tampil():
        print(f"Selamat Datang {fullname}, tugas Anda adalah:")
        global tugas
        num = 1
        for i in tugas:
            print(f"{num}.{i}")
            num += 1
        print(f"Jumlah, tugas anda sebanyak : {len(tugas)}")
        return user_input_cek()
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
user_input_cek()
user_menu()
data()
tampil()
hapus()
keluar() 
#user_input = user_input_cek()
#user_menu(user_input)