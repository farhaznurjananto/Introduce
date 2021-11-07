print("PROGRAM IDENTITAS MAHASISWA \n")

nama = "Farhaz Nurjananto"    #String karena berisikan kumpulan huruf atau karakter
nim = 212410102005            #Interger karena berisi kumpulan angka tanpa koma atau tanpa desimal
umur = 18                     #Interger karena berisi kumpulan angka tanpa koma atau tanpa desimal
tinggi_badan = 165            #Interger karena berisi kumpulan angka tanpa koma atau tanpa desimal
berat_badan = 52.5            #Float karena berisi kumpulan angka decimal
status_kejombloan = "Jomblo"  #String karena berisikan kumpulan huruf atau karakter

print("Data yan dapat dimasukkan : \nNama, NIM, Umur, Tinggi Badan, Berat Badan, Status Kejombloan, all\n")
input_user = input("Data yang ingin diketahui : ")

if input_user.lower() == "nama" :
    print(f"Nama : {nama}")
elif input_user.lower() == "nim" :
    print(f"NIM : {nim}")
elif input_user.lower() == "tinggi badan" :
    print(f"Tinggi Badan : {tinggi_badan} cm")
elif input_user.lower() == "berat badan" :
    print(f"Berat Badan : {berat_badan} kg")
elif input_user.lower() == "status kejombloan" :
    print(f"Status Kejomblohan : {status_kejombloan}")
elif input_user.lower() == "all" :
    print(f"""
    Nama              : {nama}
    NIM               : {nim}
    Umur              : {umur}
    Tinggi Badan      : {tinggi_badan} 
    Berat Badan       : {berat_badan}
    Status Kejombloan : {status_kejombloan}
    """)
else :
    print("Maaf data yang anda cari tidak ada")