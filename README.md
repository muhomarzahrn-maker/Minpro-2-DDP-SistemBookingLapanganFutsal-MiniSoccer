# Minpro-2-DDP-SistemBookingLapanganFutsal-MiniSoccer

Nama: Muhammad Omar Zahraan

NIM: 2609116023

Kelas: A

**Deskripsi Singkat Program:** 

Program ini merupakan sistem manajemen booking lapangan futsal & mini soccer yang awalnya merupakan sistem pengelolaan data sederhana menjadi versi lebih lanjut dengan penggunaan sistem hak akses (berbasis role) yang dimana lebih aman dan terstruktur. 

**Fitur Program:**

1. Program memiliki 2 tingkatan pengguna, yaitu Admin yang memiliki hak akses lengkap (CRUD) dan User yang memiliki hak akses menambah data booking dan melihat list booking.
2. Keamanan Password: Program ini menggunakan library pwinput sehingga kata sandi pengguna tidak terlihat saat melakukan login.
3. Tampilan tabel yang rapi: Program ini menggunakan library prettytable sehingga tabel yang berisi daftar transaksi booking terlihat lebih baik karena rapi.
4. Manajemen jeda: Program ini menggunakan library time untuk memberikan efek jeda transisi yang lebih responsif saat login dan keluar dari sistem.
5. Validasi input & error handling: Menerapkan kontrol percabangan untuk memastikan data (seperti jenis lapangan dan status pembayaran) diinput sesuai format, serta menangani kesalahan input angka (try-except) agar program tidak berhenti tiba-tiba.

**Tujuan Program:** 

Tujuan dari pengembangan program ini adalah untuk mempermudah dan mengoptimalkan pengelolaan sistem booking lapangan futsal dan mini soccer melalui integrasi sistem manajemen data berbasis hak akses. Program ini dirancang untuk memisahkan wewenang antara pengelola (Admin) yang memiliki kendali penuh dalam menambah, menampilkan, mengubah, dan menghapus (CRUD) data booking, serta pelanggan (User) yang dapat dengan mudah memesan dan melihat ketersediaan jadwal secara transparan. Tampilan data yang terstruktur rapi menggunakan format tabel interaktif (PrettyTable) serta keamanan autentikasi login dengan penyembunyian kata sandi (pwinput) turut meningkatkan privasi pengguna. Selain itu, penerapan validasi data dan penanganan kesalahan (error handling) secara otomatis meminimalisir risiko human error dan mencegah sistem terhenti tiba-tiba, sehingga menciptakan operasional bisnis yang lebih fleksibel, responsif, handal, dan efisien.

**Flowchart:** 




**Dokumentasi Program & Output:**

1. Login
<img width="401" height="125" alt="image" src="https://github.com/user-attachments/assets/93fbf690-0b0b-4a94-ae8a-2a85cec11285" /> 

Di atas merupakan output program yang keluar ketika kita pertama kali melakukan run. Disini kita diminta untuk memasukkan role kita (sebagai admin/user) pada foto di atas saya masuk sebagai admin, setelah memasukkan role di username masukkan password, jika sudah maka akan muncul pesan "Login berhasil! Selamat datang, (admin/user)" pesan muncul dalam beberapa detik efek dari time sleep.

2. Pilihan Menu dari Admin & User:
<img width="280" height="181" alt="Screenshot 2026-10-04 184938" src="https://github.com/user-attachments/assets/14a14a0b-5ca8-41ea-b123-4f6393772897" />
<br>
<img width="287" height="132" alt="Screenshot 2026-10-04 185030" src="https://github.com/user-attachments/assets/4b46ed29-ba8a-4c50-b313-50ae380e3ee8" />

Di atas merupakan output program yang keluar ketika kita sudah melakukan login. Pada foto pertama merupakan pilihan menu untuk admin yang dimana admin memiliki hak akses yang lebih banyak, admin memiliki akses menambah, melihat, mengubah, serta menghapus data pemesan. Pada foto kedua merupakan pilihan menu untuk user yang dimana hak aksesnya terbatas dan tidak sebanyak admin, akses user hanya menambahkan dan melihat list pemesan lapangan.

3. Menambahkan Data Booking
<img width="517" height="148" alt="Screenshot 2026-10-04 193736" src="https://github.com/user-attachments/assets/2b8cd9ae-6c19-4ca1-884a-a1fd49949c11" />

Di atas merupakan output yang keluar ketika kita memilih menu pertama pada pilihan menu (Booking Lapangan). Dimana menu ini meminta input data pemesan seperti nama pemesan, jenis lapangan yang ingin di pesan (Futsal/Mini Soccer), jam booking lapangan, dan status pembayaran kita. Jika semua data yang diminta sudah di input maka akan muncul pesan “Data berhasil ditambahkan". Menu ini dapat dijalankan oleh admin dan juga user. 

4. Menampilkan Data Pemesan Lapangan
<img width="693" height="142" alt="Screenshot 2026-10-04 194859" src="https://github.com/user-attachments/assets/bddc21be-05e0-4be4-87b3-e0157ed5cff5" />

Di atas merupakan output yang keluar ketika kita memilih menu kedua pada pilihan menu (Tampilkan Semua Booking). Di menu ini menunjukkan semua jadwal booking yang sudah di lakukan oleh pemesan di menu sebelumnya. Tetapi jika belum ada pelanggan yang melakukan booking, maka akan muncul pesan “Belum ada data booking". Pada pilihan menu ini dapat di akses oleh admin dan juga user.

5. Mengubah Data Pemesan Lapangan
<img width="686" height="250" alt="Screenshot 2026-10-04 201717" src="https://github.com/user-attachments/assets/d9baab07-e103-4a03-9b55-bdbcc97efedc" />

Di atas merupakan output yang keluar ketika memilih menu ketiga pada pilihan menu (Ubah Data Booking). Pada menu ini kita bisa mengubah data booking kita dengan memilih nomor data yang tertera pada tabel berisi list pemesan lapangan, kita dapat mengubah jenis lapangan yang ingin di pesan, mengubah jam main, dan mengubah status pembayaran. Ketika sudah selesai maka akan muncul pesan “Data berhasil diubah”. Tapi jika nomor data yang akan kita ubah tidak ditemukan/tidak ada, maka program akan menampilkan “Nomor data tidak ditemukan". Pada pilihan menu ini hanya dapat di akses oleh admin saja. 

6. Menghapus Data Pemesan Lapangan
<img width="673" height="212" alt="Screenshot 2026-10-04 202916" src="https://github.com/user-attachments/assets/e02fdaf1-2de6-49c6-b90e-0a72bc2c815a" />

Di atas merupakan output yang keluar ketika kita memilih menu ke empat pada pilihan menu (Hapus Data Booking). Dimana di menu kita bisa menghapus data booking. Pertama akan diberikan tabel berisi list pemesan, lalu pilih nomor data berapa yang ingin di hapus. Jika sudah, akan muncul pesan “Data atas nama (nama pemesan) berhasil dihapus". Tapi jika nomor data yang akan kita hapus tidak ditemukan/tidak ada, maka program akan menampilkan "Nomor data tidak ditemukan". Pada pilihan menu ini hanya dapat di akses oleh admin saja. 

7. Keluar Program
<img width="483" height="185" alt="Screenshot 2026-10-04 203337" src="https://github.com/user-attachments/assets/7b8c0032-be21-47f9-8eea-da7fa89c516c" />

Di atas merupakan output yang keluar ketika kita memilih menu ke lima pada pilihan menu (Keluar). Menu ini merupakan menu untuk mengakhiri program, program akan menampilkan pesan “Terima Kasih, semoga hari Anda Menyenangkan!” dan program akan berhenti beberapa saat setelah muncul pesan efek jeda dari time sleep.

8. Invalid Program
<img width="405" height="190" alt="Screenshot 2026-10-04 204014" src="https://github.com/user-attachments/assets/3a95efdd-5daf-40e4-bd5e-40ef15643911" />

Di atas merupakan output yang keluar jika kita menginput data yang tidak valid pada sistem. Program akan menampilkan pesan “Pilihan tidak valid, silahkan coba lagi" dan meminta kita untuk melakukan input yang benar. Ini berlaku kepada admin dan user.

**Penjelasan Nilai Tambah:** 
1. Validasi Input Menggunakan Error Handling:
<img width="488" height="50" alt="Screenshot 2026-10-04 205254" src="https://github.com/user-attachments/assets/6612be5e-b501-4dc7-b85d-57c784f88463" />

Pada program ini saya menggunakan error handling seperti pada gambar di atas. Kode ini digunakan sebagai pengelola dan menangani error pada program agar program tidak berhenti/error saat di jalankan.

3. Penerapan Library: 
<img width="355" height="70" alt="Screenshot 2026-10-04 205656" src="https://github.com/user-attachments/assets/52723b81-cb9f-4578-aaf6-ade51aa989b9" />

Pada program ini saya menerapkan 3 library di dalamnya, yaitu library time, pretty table, dan pw input. Dimana library time digunakan sebagai jeda ketika pesan muncul, library pretty table digunakan untuk list pemesan lapangan sehingga terlihat lebih rapi dan lebih baik, dan library pw input digunakan untuk kebutuhan password login. 
