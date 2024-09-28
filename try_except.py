def error():
 while True:
    try:
     user_input = int(input("Masukkan Pilihan : "))
     break
    except ValueError:
        print("Inputan harus berupa angka")  