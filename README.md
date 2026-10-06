# Minpro-2-DDP-ManajemenKoleksiEbook
Nama: Muthiara May Lista<br>
Nim: 2609116020<br>
Kelas: A'26<br>
Judul: Manajemen Koleksi Ebook<br>
Flowchart:<br>
1. Page (1)<br>
<img width="746" height="1058" alt="Page(1) drawio" src="https://github.com/user-attachments/assets/8a901004-b8b3-48c8-a061-f2c48c4b7eb7" /><br>
<br>
Penejelasan:<br>
Pada page pertama akan dimulai, dilanjutkan dengan Inisialisasi seluruh Data, dilanjutkan dengan diminta untuk menginput Username & Pasword setelahnya akan di proses ke bagian admin/user. Dilanjutkan decision apakah username sesuai dengan data jika `tidak`/`kososng` maka akan di tampilkan username kosong/salah dan akan kembali untuk menginput username lagi, jika `benar` maka dilanjutkan dengan decision apakah password sesuai dengan data jika `tidak`/`kosong` maka akan di tampilkan username kosong/salah dan akan kembali untuk menginput password lagi, `benar` maka akan di tampilkan output login sukses.<br>
<br>
Dilanjutkan dengan menampilkan pilihan kategori dan menginput pilihan kategori(angka) lanjut ke decision pilihan jika memilih 1,2 & 3 maka akan lanjut ke corrector menu, jika meimilih pilihan 4 maka akan ditampilkan "program selesai" dan berakhir. Dan jika memilih diluar pilihan maka ditampilkan "pilihan kategori tidak ada" dan akan kembali untuk memilih kategori lagi.<br>
2. Page (2)<br>
<img width="690" height="1049" alt="Page(2) drawio" src="https://github.com/user-attachments/assets/4d8cae78-674a-4acd-ad4d-e473b9061fb2" /><br>
Penejelasan:<br>
Dilanjutkan ke decision jika `benar` admin maka akan mempunyai 5 pilihan yaitu CRUD, jika `tidak` maka ototmatis masuk ke menu user yang hanya mempunyai 2 pilihan menu.<br>
<br>
#Admin<br>
Pada admin harus menginput pilihan diantara CRUD tersebut, masuk pada bagian deicision untuk pilihan 1, 2, 3, dan 4 akan di teruskan kepada masing-masing corrector di pilihan tersebut dan pada pilihan ke 5  akan kembali ke daftar kategori. Dan jika memasukkan angka yang tidak ada dipilihan maka akan menampilkan "Pilihan menu tidak ada" dan akan kembali ke daftar kategori.<br>
<br>
#User<br>
Pada user harus menginput pilihan diantar 2 pilihan yaitu lihat ebook atau kembali ke kategori, dan jika memasukkan angka yang tidak ada dipilihan maka akan menampilkan "Pilihan menu tidak ada" dan akan kembali ke daftar kategori.<br>
<br>
3. Page (3)<br>
<img width="570" height="692" alt="Page(3) drawio" src="https://github.com/user-attachments/assets/e34461e6-f588-4a24-bd29-c98b8bcef713" /><br>
Penejelasan:<br>
#1<br>
Pada pilihan satu akan menampilkan seluruh daftar ebook awal dan akan kembali ke daftar kategori.<br>
#2<br>
Pada pilihan kedua akan masuk untuk menginput judul baru, lanjut ke decision jika judul kosong maka akan muncul tampilan "Judul tidak boleh ksoong" dan kembali untuk menginput judul baru dan jika telah menginput judul baru melanjutkan untuk menginput penulis baru. Jika judul penulis maka akan muncul tampilan "Penulis tidak boleh kosong" dan kembali untuk menginput penulis baru dan jiika  telah berhasil menginput penulis bary maka akan ada tampilan "Ebook berhasil ditambah" dan akan ditampilkan daftar ebook yang baru setelahnya kembali ke kategori.<br>
<br>
4. Page (4)<br>
<img width="650" height="1065" alt="Page (4) drawio" src="https://github.com/user-attachments/assets/c88fe29c-1b31-4358-88e4-a5d09dc2a4ff" /><br>
Penjelasan:<br>
#3<br>
Pada pilihan ketiga ditampilkan terlebih dahulu daftar ebook yang lama lalu diminta untuk menginput judul lama yang ingin diubah, jika kosong akan muncul tampilan "judul lama tidak boleh kosong" dan kembali untuk menginput judul lama. Jika telah mengisi judul lama akan lanjut untuk menginput penulis lama yang ingin di ubah dan sama jika kosong akan muncul tampilan "penulis lama tidak boleh kosong" dan kembali untuk menginput penulis lama.<br>
Dilanjutkan untuk menginput judul baru dan penulis baru dan sama juga jika salah satu kosong maka akan muncul tampilan "judul/penulis baru tidak boleh kosong" dan kembali untuk menginput judul/penulis baru. Dan jika telah menginput judul & penulis baru maka akan menampilkan daftar ebook baru dan menampilkan kalimat "Ebook berhasil diubah"<br>
#4<br>
Pada pilihan keempat ditampilkan terlebih dahulu daftar ebook yang lalu diminta untuk menginput judul ebook yang ingin dihapus, jika kosong akan muncul tampilan "judul yang ingin dihapus tidak boleh kosong" dan kembali untuk menginput judul yang ingin di hapus. Jika telah mengisi judul akan lanjut untuk menginput penulis yang ingin di hapus dan sama jika kosong akan muncul tampilan "penulis yang ingin dihapus tidak boleh kosong" dan kembali untuk menginput penulis yang ingin dihapus.<br>
<br>
CODE:
1. Input<br>
<img width="229" height="79" alt="image" src="https://github.com/user-attachments/assets/e3faf8e2-aff8-4519-a25b-1b6e204bc593" /><br>
Dengan import pwinput untuk mengimpor library pwinput untuk password, def kosong untuk mendefinisikan jika terdapat data kosong maka akn terbaca kosong dan return data == "" untuk mengembalikan boolean true jika bener" kosong dan jika false jika tidak kosong.<br>
<br>
<img width="509" height="284" alt="image" src="https://github.com/user-attachments/assets/46737a84-7f9e-4332-a453-04b578e32133" /><br>
Terdapat ebooks seabagai list yang berisikan tuple dalamnya untuk menyimpan data kategori ebook, dan pada masing masing kategori berisikan data 3 judul & penulis ebook yang sesuai tentang kategori.<br>
Ouput:<br>
2. Input<br>
<img width="320" height="194" alt="image" src="https://github.com/user-attachments/assets/c645267c-6e85-4c53-b7b8-959cfcd08474" /><br>
Dengan Varibel dictionary dengan nama `akun` penyimpan data nested dictionary untuk mengelola pengguna yang berisikan nama, password dan akses untuk ke menu bagian admin/user.<br>
<br>
<img width="461" height="493" alt="image" src="https://github.com/user-attachments/assets/8f240752-9b0f-4f4d-8fa9-9104682785e9" /><br>
Dengan while true untuk melakukan perulangahn untuk mengsi username & password login dan jika username/password maka akan menampilkan "username/password tidak boleh kosong" dan dengan fungsi continue untuk mengulang perulangan. Pada password akan terlihat karakter *** (bintang) dengan menggunakan fungsi pwinput untuk menyembunyikan karakter password pengguna.<br>
Dan jika username/password salah maka akan ditampilkan "Username/password salah" dan dengan fungsi continue untuk mengulang perulangan. Dan dengan `akses = login()` untuk memanggil fungsi login () dn menyiman nilai hasil pengembaliannya dalam variabel akses<br>
Output:<br>
3. Input<br>
<img width="592" height="71" alt="image" src="https://github.com/user-attachments/assets/c5b53d07-f164-4e6c-b601-120a031e04db" /><br>
Pada pilihan 1 akan bisa di akses sama admin & user dengan mendefinisikan lihat_ebook dan dengan menampilkan daftar ebook awal dengan menggunakan indeks 0 dan 1 untuk menampilkan ebook dan penulis.<br>
Output::<br>
<img width="625" height="327" alt="image" src="https://github.com/user-attachments/assets/0e93a58e-4a41-4c66-9729-d28557510d08" /><br>
Pada pilihan 2 akan bisa di akses oleh admin saja dengan mendefinsikan tambah_ebook dengan menggunakan while true untuk mengisi data pengguna mulai dari judul dan penulis jika kosong maka akan menampilkan "Judul/Penulis tidak boleh kosong"













   
