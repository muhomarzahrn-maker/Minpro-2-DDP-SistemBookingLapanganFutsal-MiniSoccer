import time
from prettytable import PrettyTable
import pwinput

users = {
    "admin": {"password": "123", "role": "admin"},
    "user": {"password": "456", "role": "user"}
}

list_booking = []

def login():
    print("=== LOGIN SYSTEM ===")
    while True:
        username = input("Username: ").strip()
        password = pwinput.pwinput("Password: ").strip()

        if username in users and users[username]["password"] == password:
            print(f"\nLogin berhasil! Selamat datang, {username}.")
            time.sleep(1)
            return username, users[username]["role"]
        else:
            print("Username atau password salah! Silakan coba lagi.\n")

def tampilkan_booking():
    print("\n[DAFTAR BOOKING]")
    if not list_booking:
        print("Belum ada data booking.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama Pemesan", "Jenis Lapangan", "Jam Booking", "Status Pembayaran"]
        for index, item in enumerate(list_booking, start=1):
            tabel.add_row([index, item["nama"], item["lapangan"], item["jam"], item["status"]])
        print(tabel)

def tambah_booking():
    print("\n[BOOKING LAPANGAN]")
    nama = input("Masukkan nama pemesan: ").strip()
    
    while True:
        lapangan = input("Masukkan jenis lapangan (Futsal/Mini Soccer): ").strip()
        if lapangan.lower() in ["futsal", "mini soccer"]:
            break
        print("Input tidak valid! Harap pilih antara 'Futsal' atau 'Mini Soccer'.")

    jam = input("Masukkan jam booking (contoh: 16:00): ").strip()
    
    while True:
        status = input("Masukkan status pembayaran (Lunas/DP/Belum): ").strip()
        if status.lower() in ["lunas", "dp", "belum"]:
            break
        print("Input tidak valid! Harap pilih antara 'Lunas', 'DP', atau 'Belum'.")

    data = {
        "nama": nama,
        "lapangan": lapangan,
        "jam": jam,
        "status": status
    }
    list_booking.append(data)
    print("Data berhasil ditambahkan.")

def ubah_booking():
    print("\n[UBAH DATA LAPANGAN & PEMBAYARAN]")
    if not list_booking:
        print("Belum ada data untuk diubah.")
        return

    tampilkan_booking()
    
    try:
        index = int(input("Pilih nomor data yang ingin diubah: ")) - 1
        if 0 <= index < len(list_booking):
            nama_lama = list_booking[index]["nama"]
            
            while True:
                lapangan_baru = input("Masukkan jenis lapangan baru (Futsal/Mini Soccer): ").strip()
                if lapangan_baru.lower() in ["futsal", "mini soccer"]:
                    break
                print("Input tidak valid! Harap pilih antara 'Futsal' atau 'Mini Soccer'.")

            jam_baru = input("Masukkan jam baru: ").strip()
            
            while True:
                status_baru = input("Masukkan status pembayaran baru (Lunas/DP/Belum): ").strip()
                if status_baru.lower() in ["lunas", "dp", "belum"]:
                    break
                print("Input tidak valid! Harap pilih antara 'Lunas', 'DP', atau 'Belum'.")

            list_booking[index] = {
                "nama": nama_lama,
                "lapangan": lapangan_baru,
                "jam": jam_baru,
                "status": status_baru
            }
            print("Data berhasil diubah.")
        else:
            print("Nomor data tidak ditemukan.")
    except ValueError:
        print("Error: Input harus berupa angka!")

def hapus_booking():
    print("\n[HAPUS DATA BOOKING]")
    if not list_booking:
        print("Belum ada data untuk dihapus.")
        return

    tampilkan_booking()
    
    try:
        index = int(input("Pilih nomor data yang ingin dihapus: ")) - 1
        if 0 <= index < len(list_booking):
            data_dihapus = list_booking.pop(index)
            print(f"Data atas nama {data_dihapus['nama']} berhasil dihapus.")
        else:
            print("Nomor data tidak ditemukan.")
    except ValueError:
        print("Error: Input harus berupa angka!")

def menu_admin():
    while True:
        print("\n--- MENU ADMIN ---")
        print("1. Booking Lapangan")
        print("2. Tampilkan Semua Booking")
        print("3. Ubah Data Booking")
        print("4. Hapus Data Booking")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            tambah_booking()
        elif pilihan == "2":
            tampilkan_booking()
        elif pilihan == "3":
            ubah_booking()
        elif pilihan == "4":
            hapus_booking()
        elif pilihan == "5":
            print("Terima kasih Admin, semoga hari Anda menyenangkan!")
            time.sleep(1)
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

def menu_user():
    while True:
        print("\n--- MENU USER ---")
        print("1. Booking Lapangan")
        print("2. Tampilkan Semua Booking")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ").strip()

        if pilihan == "1":
            tambah_booking()
        elif pilihan == "2":
            tampilkan_booking()
        elif pilihan == "3":
            print("Terima kasih, semoga hari Anda menyenangkan!")
            time.sleep(1)
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

def main():
    username, role = login()
    
    if role == "admin":
        menu_admin()
    else:
        menu_user()

if __name__ == "__main__":
    main()