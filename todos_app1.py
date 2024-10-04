user_input = int
tugas = []
def name():
    print("-------------------")
    print("APLIKASI TO-DO LIST")
    print("-------------------\n")
    nama = input("Masukkan Nama Depan : ")
    nama1 = input("Masukkan Nama Belakang : ")
    return f"{nama} {nama1}"

def tampilnama(fullname):
    print(f"\n Selamat Datang {fullname} \n") 

fullname = name()
tampilnama(fullname)
   
def menu():
    print("1. Tambahkan Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

def data():
    todo = input(f"Masukkan Tugas: ")
    while todo.lower() != "stop":
        tugas.append(todo)
        todo = input(f"Masukkan Tugas: ")
        

def hapus():
    tugas_hapus = int(input("Hapus Tugas ke : ")) - 1
    tugas.pop(tugas_hapus)
    

def tampil():
        #print(f"Selamat Datang {fullname}, tugas Anda adalah:")
        num = 1
        print(f"Berikut tugas Anda:")
        for i in tugas:
            print(f"{num}.{i}")
            num += 1
        print(f"Halo {fullname}, jumlah tugas anda sebanyak : {len(tugas)}\n")
        

def keluar():    
    exit_ = input("Apakah anda ingin keluar (y/n) : ")
    if exit_ == 'y':
        print("Terima Kasih")
        exit()
    else:
        print("Silahkan tambahkan tugas anda: ")
        data()
        tampil()

     
def main():
  while True:
    menu()
    try:
            user_input = int(input("Masukkan Pilihan : "))
            if user_input == 4:
                keluar()
            if user_input in [1,2,3]:
                if user_input == 1:
                    #print("1. Tambahkan Tugas")
                    data()
                elif user_input == 2:
                    tampil()
                    print("2. Lihat Tugas")
                    try:
                     if not tugas:
                        print("Belum ada tugas\n")
                        return main()
                    except NameError:
                        print("Masukkan tugas anda terlebih dahulu")          
                elif user_input == 3:
                    if not tugas:
                        print("Belum ada tugas")
                        return main()
                    else:
                     hapus()
    except ValueError:
        print("Inputan harus berupa angka")


if __name__ == "__main__":
 main()