ktp = {"Namalengkap":"Jajang Miharja", 
       "NIK" : 1234567,
       "Tempat_lahir" : "Bandung",
       "Agama" : "Islam",
       "Jenis_kelamin" : "Laki-laki",
       "Pekerjaan" : "Mahasiswa",
       "Status" : "Belum_Menikah",
       "alamat" : {"Jalan" : "Jl. Raya Cibiru",
                   "Kecamatan" : "Cibiru",
                   "Kota" : "Bandung",
                   "Provinsi" : "Jawa Barat"},
       "Hobi" : ["baca", "makan", "tidur"]}


ala = ktp.get("alamat").get("Kecamatan")
ala1 = (ktp.get("alamat")["Kecamatan"])

ktp["NIK"] = 67890345
ktp["Jenis_kelamin"] = "Laki-laki"
ktp["alamat"]["Kecamatan"] = "Ciwideuw"

new_hobi = "menulis"
ktp["Hobi"].append(new_hobi)
print(ktp)