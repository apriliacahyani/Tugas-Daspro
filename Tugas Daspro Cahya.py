listfilm = {
    'action':{1:'Black Adam', 2: 'Star Wars', 3: 'Guardians of the Galaxy', 4: 'John Wick', 5: 'The Beekeper'},
    'comedy':{1: 'Kapan Kawin', 2: 'Orang Kaya Baru', 3: 'My Stupid Boss', 4: 'Agak Laen'},
    'fantasy':{1: 'The Chronicles of Narnia', 2: 'Wonka', 3: 'Cinderella', 4: 'Beauty and the Beast'},
    'thriller':{1: 'Parasite', 2: 'Joker', 3: 'Bird Box', 4: 'Plane', 5: 'Oppenheimer'},
}
waktufilm = {1: '08:00 WIT - 09:50 WIT',2: '14:30 WIT - 16:20 WIT',3: '21:00 WIT - 22:50 WIT',}

namapembuattugas = {
    '1':{'Aprilia Cahyani': '07352311018'},

}
# harinonton = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
import datetime
tanggal = datetime.datetime.now()
hari = tanggal.strftime('%A')

namapembeli = []
umurpembeli = []
tidakcukupumur = []
    
def garis():
    print('==============================')
while True:
    print('Selamat datang')
    garis()
    print('1. Pesan tiket')
    print('2. lihat tiket yang dipesan')
    print('3. lihat bio pembuat tugas')
    print('4. Exit')
    pilihan = input('Apa yang ingin anda lakukan?: ')
    if pilihan == '1' or pilihan.lower() == 'pesan tiket':
        while True:
            print('Pilih genre film:')
            garis()
            print('Genre film:')
            for genre, judul in listfilm.items():
                print(f'--> {genre}')
            garis()
            pilih = input('Pilih genre Film: ')
            print('')
            for genre, judul in listfilm.items():
                if pilih.lower() in listfilm and pilih.lower() != genre:
                    continue
                elif pilih.lower() == genre:
                    while True:
                        print('Silahkan pilih film:')
                        garis()
                        print(f'Daftar film {pilih.lower()}: ')
                        for number, film in judul.items():
                            print(f'{number}. {film}')
                        garis()    
                        pilihfilm = int(input(f'Pilih film yang ingin di tonton (1-{len(judul)}): '))
                        print('')
                        for number, film in judul.items():
                            if pilihfilm != number and pilihfilm in judul:
                                continue
                            elif pilihfilm == number:
                                while True:
                                    print('Jam tayang:')
                                    garis()
                                    for x, waktu in waktufilm.items():
                                        print(f'{x}. {waktu}')        
                                    jamtayang = int(input(f'Pilih jam tayang (1-{len(waktufilm)}): '))
                                    for x, waktu in waktufilm.items():
                                        if jamtayang != x and jamtayang in waktufilm:
                                            continue
                                        elif jamtayang == x:
                                            print('')
                                            while True:
                                                print('Detail film: ')
                                                garis()
                                                print(f'Nama film\t: {film}')
                                                print(f'Genre film\t: {genre}')
                                                print(f'Waktu film\t: {waktu}')
                                                if hari == 'Sunday':
                                                    hargatiket = 50000
                                                elif hari == 'Saturday':
                                                    hargatiket = 45000
                                                else:
                                                    hargatiket = 35000
                                                print(f'Harga tiket\t: Rp. {hargatiket}')
                                                garis()
                                                konfirmasi = input('Ingin membeli tiket? (ya/tidak): ')
                                                print('')
                                                if konfirmasi == 'ya':
                                                    jumlahtiket = int(input('Masukkan jumlah tiket: '))
                                                    print('')
                                                    for item in range(jumlahtiket):
                                                        print(f'Bio {item+1}: ')
                                                        garis()
                                                        nama = input('Masukkan nama: ')
                                                        namapembeli.append(nama)
                                                        umur = int(input('Masukkan umur: '))
                                                        umurpembeli.append(umur)
                                                        if umur < 18 :
                                                            namapembeli.remove(nama)
                                                            umurpembeli.remove(umur)
                                                            tidakcukupumur.append(nama)
                                                            print('Maaf anda tidak bisa membeli tiket')
                                                        print('')
                                                    if len(namapembeli) < jumlahtiket :
                                                        for i in range(len(tidakcukupumur)):    
                                                            print(f'{tidakcukupumur[i]} tidak dapat menonton')
                                                        garis()    
                                                        confirm = input('Ingin melanjutkan? (ya/tidak): ')
                                                        if confirm == 'ya':
                                                            print('\nInvoice ticket:')        
                                                            print(f'Quantity: {len(namapembeli)} orang')
                                                            for i in range(len(namapembeli)):
                                                                garis()
                                                                print('Nama :', namapembeli[i])
                                                                print('Usia :', umurpembeli[i], 'tahun')
                                                                print('Film :', film)
                                                                print('Waktu:', waktu)
                                                                garis()
                                                            tidakcukupumur.clear()
                                                        else:
                                                            print('Baiklah, terimakasih sudah singgah')
                                                            tidakcukupumur.clear()
                                                            break
                                                        break
                                                    else:
                                                        confirm = input('Ingin melanjutkan? (ya/tidak): ')
                                                        if confirm == 'ya':
                                                            print('\nInvoice ticket:')        
                                                            print(f'Quantity: {jumlahtiket} orang')
                                                            for i in range(jumlahtiket):
                                                                garis()
                                                                print('Nama :', namapembeli[i])
                                                                print('Usia :', umurpembeli[i], 'tahun')
                                                                print('Film :', film)
                                                                print('Waktu:', waktu)
                                                                garis()
                                                            tidakcukupumur.clear()
                                                            break
                                                        else:
                                                            print('Baiklah, terimakasih sudah singgah')
                                                            tidakcukupumur.clear()
                                                            break
                                                        
                                                else:
                                                    print('Terimkasih sudah singgah')
                                                    break
                                        else:
                                            print('\nPilih jam tayang dengan benar!')
                                            break
                                    confirm = input('Ingin kembali? (ya/tidak): ')
                                    if confirm == 'ya':
                                        print('')
                                        break
                                    else:
                                        confirm= input('Pilih jam tayang? (ya/tidak): ')
                                        if confirm == 'ya':
                                            print('')
                                            continue
                                        else:
                                            break
                            else:
                                print('Angka yang dimasukkan tidak sesuai')
                                break
                        confirm = input('Pilih film? (ya/tidak): ')
                        if confirm == 'ya':
                            print('')
                        else:
                            confirm = input('Kembali? (ya/tidak): ')
                            if confirm == 'ya':
                                break               
                else:
                    print('Harap masukkan keyword dengan benar!!')
                    break
            confirm = input('Ingin mengisi kembali? (ya/tidak): ')
            if confirm == 'ya':
                print('')
                continue
            else:
                print('')
                break
    elif pilihan == '2' or pilihan.lower() == 'lihat tiket yang dipesan':
        while True:
            print(f'{len(namapembeli)} ticket dipesan')
            for i in range(len(namapembeli)):
                print('Bio', i+1)
                garis()
                print('Nama :', namapembeli[i])
                print('Usia :', umurpembeli[i], 'tahun')
                print('Film :', film)
                print('Waktu:', waktu)
                garis()
            confirm = input('Ingin kembali? (ya/tidak): ')
            if confirm == 'ya':
                print('')
                break

    elif pilihan == '3' or pilihan.lower() == 'lihat nama kelompok':
        while True:
            print('Nama kelompok: ')
            garis()
            for nomor, info in namapembuattugas.items():
                print('Pembuat Tugas : ')
                for nama, npm in info.items():
                    print(f'Nama: {nama}')
                    print(f'NPM : {npm}')
            confirm = input('Kembali? (ya/tidak): ')
            if confirm == 'ya':
                print('')
                break
            else:
                continue
    elif pilihan == '4' or pilihan.lower() == 'exit':
        print('Program selesai')
        print('Anda telah keluar')
        break
    else:
        print('')
        print('Pilihan tidak valid, silahkan pilih lagi')