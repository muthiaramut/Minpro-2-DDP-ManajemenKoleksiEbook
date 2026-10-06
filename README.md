# Minpro-2-DDP-ManajemenKoleksiEbook
Nama: Muthiara May Lista<br>
Nim: 2609116020<br>
Kelas: A'26<br>
Judul: Manajemen Koleksi Ebook<br>
<br>
Flowchart:<br>
<br>
1. Page (1)<br>
<img width="746" height="1058" alt="Page(1) drawio" src="https://github.com/user-attachments/assets/8a901004-b8b3-48c8-a061-f2c48c4b7eb7" /><br>
<br>
Penejelasan:<br>
Pada page pertama akan dimulai, dilanjutkan dengan Inisialisasi seluruh Data, dilanjutkan dengan diminta untuk menginput Username & Pasword setelahnya akan di proses ke bagian admin/user. Dilanjutkan decision apakah username sesuai dengan data jika `tidak`/`kososng` maka akan di tampilkan username kosong/salah dan akan kembali untuk menginput username lagi, jika `benar` maka dilanjutkan dengan decision apakah password sesuai dengan data jika `tidak`/`kosong` maka akan di tampilkan username kosong/salah dan akan kembali untuk menginput password lagi, `benar` maka akan di tampilkan output login sukses.<br>
<br>
Dilanjutkan dengan menampilkan pilihan kategori dan menginput pilihan kategori(angka) lanjut ke decision pilihan jika memilih 1,2 & 3 maka akan lanjut ke corrector menu, jika meimilih pilihan 4 maka akan ditampilkan "program selesai" dan berakhir. Dan jika memilih diluar pilihan maka ditampilkan "pilihan kategori tidak ada" dan akan kembali untuk memilih kategori lagi.<br>
<br>
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
<br>
#2<br>
Pada pilihan kedua akan masuk untuk menginput judul baru, lanjut ke decision jika judul kosong maka akan muncul tampilan "Judul tidak boleh ksoong" dan kembali untuk menginput judul baru dan jika telah menginput judul baru melanjutkan untuk menginput penulis baru. Jika judul penulis maka akan muncul tampilan "Penulis tidak boleh kosong" dan kembali untuk menginput penulis baru dan jiika  telah berhasil menginput penulis bary maka akan ada tampilan "Ebook berhasil ditambah" dan akan ditampilkan daftar ebook yang baru setelahnya kembali ke kategori.<br>
<br>
4. Page (4)<br>
<img width="650" height="1065" alt="Page (4) drawio" src="https://github.com/user-attachments/assets/c88fe29c-1b31-4358-88e4-a5d09dc2a4ff" /><br>
Penjelasan:<br>
#3<br>
Pada pilihan ketiga ditampilkan terlebih dahulu daftar ebook yang lama lalu diminta untuk menginput judul lama yang ingin diubah, jika kosong akan muncul tampilan "judul lama tidak boleh kosong" dan kembali untuk menginput judul lama. Jika telah mengisi judul lama akan lanjut untuk menginput penulis lama yang ingin di ubah dan sama jika kosong akan muncul tampilan "penulis lama tidak boleh kosong" dan kembali untuk menginput penulis lama.<br>
<br>
Dilanjutkan untuk menginput judul baru dan penulis baru dan sama juga jika salah satu kosong maka akan muncul tampilan "judul/penulis baru tidak boleh kosong" dan kembali untuk menginput judul/penulis baru. Dan jika telah menginput judul & penulis baru maka akan menampilkan daftar ebook baru dan menampilkan kalimat "Ebook berhasil diubah"<br>
<br>
#4<br>
Pada pilihan keempat ditampilkan terlebih dahulu daftar ebook yang lalu diminta untuk menginput judul ebook yang ingin dihapus, jika kosong akan muncul tampilan "judul yang ingin dihapus tidak boleh kosong" dan kembali untuk menginput judul yang ingin di hapus. Jika telah mengisi judul akan lanjut untuk menginput penulis yang ingin di hapus dan sama jika kosong akan muncul tampilan "penulis yang ingin dihapus tidak boleh kosong" dan kembali untuk menginput penulis yang ingin dihapus.<br>
<br>
CODE:
<br>
1. Input<br>
<img width="229" height="79" alt="image" src="https://github.com/user-attachments/assets/e3faf8e2-aff8-4519-a25b-1b6e204bc593" /><br>
Dengan import pwinput untuk mengimpor library pwinput untuk password, def kosong untuk mendefinisikan jika terdapat data kosong maka akn terbaca kosong dan return data == "" untuk mengembalikan boolean true jika bener" kosong dan jika false jika tidak kosong.<br>
<br>
<img width="509" height="284" alt="image" src="https://github.com/user-attachments/assets/46737a84-7f9e-4332-a453-04b578e32133" /><br>
Terdapat ebooks seabagai list yang berisikan tuple dalamnya untuk menyimpan data kategori ebook, dan pada masing masing kategori berisikan data 3 judul & penulis ebook yang sesuai tentang kategori.<br>
<br>
Ouput:<br>
1. Daftar Kategori Ebook<br>
<img width="229" height="119" alt="image" src="https://github.com/user-attachments/assets/d54eea84-1ba9-4ce0-b172-7df907ad56c6" /><br>
2. Daftar ebook `Pembelajaran`<br>
<img width="223" height="69" alt="image" src="https://github.com/user-attachments/assets/bf949d7d-e3cf-441d-9951-d5db65cb1e42" /><br>
3. Daftar ebook `Penelitian`<br>
<img width="287" height="77" alt="image" src="https://github.com/user-attachments/assets/3b27b202-45ff-4769-bd8d-c109f218db7d" /><br>
4. Daftar ebook `Novel`<br>
<img width="236" height="76" alt="image" src="https://github.com/user-attachments/assets/42921f5e-c05e-4f93-89e9-3e28a01e3452" />
<br>
4. Input<br>
<img width="320" height="194" alt="image" src="https://github.com/user-attachments/assets/c645267c-6e85-4c53-b7b8-959cfcd08474" /><br>
Dengan Varibel dictionary dengan nama `akun` penyimpan data nested dictionary untuk mengelola pengguna yang berisikan nama, password dan akses untuk ke menu bagian admin/user.<br>
<br>
<img width="461" height="493" alt="image" src="https://github.com/user-attachments/assets/8f240752-9b0f-4f4d-8fa9-9104682785e9" /><br>
Dengan while true untuk melakukan perulangahn untuk mengsi username & password login dan jika username/password maka akan menampilkan "username/password tidak boleh kosong" dan dengan fungsi continue untuk mengulang perulangan. Pada password akan terlihat karakter *** (bintang) dengan menggunakan fungsi pwinput untuk menyembunyikan karakter password pengguna.<br>
<br>
Dan jika username/password salah maka akan ditampilkan "Username/password salah" dan dengan fungsi continue untuk mengulang perulangan. Dan dengan `akses = login()` untuk memanggil fungsi login () dn menyiman nilai hasil pengembaliannya dalam variabel akses<br>
Output:<br>
Ouput:<br>
1. Username benar sebagai admin<br>
<img width="258" height="185" alt="image" src="https://github.com/user-attachments/assets/81ebd286-c7c4-4403-8dcc-70f89886028b" /><br>
2. Password benar sebagai user<br>
<img width="306" height="181" alt="image" src="https://github.com/user-attachments/assets/7fbded93-8ba4-454e-9f02-820982142981" /><br>
3. Jika Username & password kosong<br>
<img width="417" height="143" alt="image" src="https://github.com/user-attachments/assets/987a5c53-db2c-4c2b-959c-f183a2095793" /><br>
4. Jika Username & Password salah<br>
<img width="349" height="142" alt="image" src="https://github.com/user-attachments/assets/896a47f3-1380-4c7c-b62b-44cf8c742ef8" /><br>
<br>
3. Input<br>
<img width="592" height="71" alt="image" src="https://github.com/user-attachments/assets/c5b53d07-f164-4e6c-b601-120a031e04db" /><br>
Pada pilihan 1 bisa di akses admin & user dengan mendefinisikan lihat_ebook dan dengan menampilkan daftar ebook awal dengan menggunakan indeks 0 dan 1 untuk menampilkan ebook dan penulis dan setelahnya akan mengulang kembali memilih kategori kembali.<br>
<br>
Output::<br>
<img width="221" height="335" alt="image" src="https://github.com/user-attachments/assets/201fa124-15c5-4017-bc58-913075f2ac14" /><br>
<br>
4. Input<br>
<img width="625" height="327" alt="image" src="https://github.com/user-attachments/assets/0e93a58e-4a41-4c66-9729-d28557510d08" /><br>
Pada pilihan 2 akan bisa di akses oleh admin saja dengan mendefinsikan tambah_ebook dengan menggunakan while true untuk mengisi data pengguna mulai dari judul dan penulis jika kosong maka akan menampilkan "Judul/Penulis tidak boleh kosong" dan akan mengulang untuk mengisi inputan judul/penulis. Dan setelah menginput judul dan penulis yang ingin ditambahkan dengan menggunakan `append` maka akan otomatis masuk kedalam list ebooks lalu menampilkan "Ebook ditambahkan" dan akan menampilkan daftar ebook terbaru.<br>
<br>
Output:<br>
<img width="289" height="355" alt="image" src="https://github.com/user-attachments/assets/8afb9538-58ed-4a05-b4ae-d6930df96598" /><br>
<br>
5. Input<br>
<img width="645" height="625" alt="image" src="https://github.com/user-attachments/assets/0c477e90-8ccf-485c-ac49-8d3d6571e095" /><br>
Pada pilihan 3 akan bisa di akses oleh admin saja dimulai dengan ditampilkan daftar ebook terbaru untuk melihat data ebook yang ingin di ubah , lalu dengan mendefinisikan ubah_ebook dengan menggunakan while true untuk mengsi data pengguna dengan memasukkan judul/penulis yang lama, jika judul dan penulis jika kosong maka akan menampilkan "Judul/Penulis tidak boleh kosong" dan akan mengulang untuk mengisi inputan judul/penulis yang ingin di ubah. Dengan `remove` maka data yang di input akan otomatis terhapus dari list data ebooks.
<dr>
Dilanjutkan dengan mengisi juduk dan penulis baru yang ingin di masukkan ke dalam data untuk mengubah data yang lama, lalu jika judul dan penulis jika kosong maka akan menampilkan "Judul/Penulis tidak boleh kosong" dan akan mengulang untuk mengisi inputan judul/penulis yang ingin di tambah. Digunakan peran `append` untuk menambahkan data di list ebooks sesuai data yang baru. Setelah berhasil maka akan menampilkan kalimat "Ebook berhasil diubah" dan menampilkan kembali daftar ebook terbaru.<br>
<br>
Output:<br>
<img width="354" height="527" alt="image" src="https://github.com/user-attachments/assets/fac09c7f-d388-41eb-8c52-688bf5236715" /><br>
<br>
6. Input<br>
<img width="637" height="525" alt="image" src="https://github.com/user-attachments/assets/f4f69da9-8007-450f-adff-5c01aab7ad29" /><br>
Pada pilihan ke 4 yang hanya bisa di akses oleh admin dengan menggunakan while true untuk mengsi data pengguna dimulai dengan di tampilkan daftar ebook terbaru lalu menginput judul/penulis yang ingin di hapus, jika judul dan penulis jika kosong maka akan menampilkan "Judul/Penulis tidak boleh kosong" dan akan mengulang untuk mengisi inputan judul/penulis yang ingin di dihapus. Lalu kembali menggunakan peran `remove` untuk menghapus data yang diinput untuk di hapus dari data list ebooks. Lalu setelahnya akan menampilkan ebook terbaru dan menampilkan kalimat "Ebook berhasil dihapus"<br>
<br>
Output:<br>
<img width="437" height="489" alt="image" src="https://github.com/user-attachments/assets/c0666e48-4d92-4e63-b00c-6cf3d3060939" /><br>
<br>
7. Input<br>
<img width="643" height="504" alt="image" src="https://github.com/user-attachments/assets/805d55f9-1123-4b84-98d3-fff81a24daaa" /><br>
Ini adalah perulangan untuk menampilkan Pilihan Kategori dengan menggunakan indeks jika memilih 1,2,3 maka indeks data `0,1,2` yang akan ditampilkan, jika memilih kategori 4 maka akan keluar dari program dan menampilkan "Program Selesai" dan jika pengguna memasukkan kategori yang lain maka akan menampilkan ouput "Pilihan Kategori tidak ada" dan kembali untuk memilih kategori lagi.
<br>
Output:<br>
1. Jika memilih pilihan 4<br>
<img width="255" height="143" alt="image" src="https://github.com/user-attachments/assets/80b3b2b4-b253-453f-b42b-acfa0f6ca597" /><br>
2. Jika memeilih diluar pilihan<br>
<img width="285" height="228" alt="image" src="https://github.com/user-attachments/assets/ba6fe414-d005-4064-b545-453dfdce7a82" /><br>
<br>
8. Input<br>
<img width="466" height="515" alt="image" src="https://github.com/user-attachments/assets/c4355348-8d64-496f-8d2b-eaff4aab8781" /><br>
Untuk menampilkan dan memanggil akses yang hanya bisa di lakukan admin ebook yaitu dapat melakukan CRUD, jika memasukkan angka diluar pilihan maka akan kembali memilih kategori.<br>
1. Jika memilih pilihan 5<br>
<img width="331" height="228" alt="image" src="https://github.com/user-attachments/assets/7da2ab47-c365-4cd9-8a5a-8c15aebcc427" /><br>
<br>
2. Jika memilih diluar pilihan<br>
<img width="277" height="225" alt="image" src="https://github.com/user-attachments/assets/aaa8a506-2e19-494c-bff4-8eb7c64ed0f9" /><br>
3. Jika tidak memilih kategori menu pilihan<br>

<br>
9. Input<br>
<img width="607" height="296" alt="image" src="https://github.com/user-attachments/assets/66b2f30a-12fa-4caf-8d1b-8895861c1623" /><br>
Untuk menampilkan dan memanggil akses yang hanya bisa di lakukan user ebook yaitu hanya dapat melihat ebook atau kembali memilih kategori jika memasukkan angka diluar pilihan maka akan kembali memilih kategori.<br>
1. Jika memilih pilihan 2<br>
<img width="299" height="299" alt="image" src="https://github.com/user-attachments/assets/69c07f96-dc59-412b-a76f-c72a159a2163" /><br>
<br>
2. Jika memilih diluar pilihan<br>
<img width="229" height="89" alt="image" src="https://github.com/user-attachments/assets/dc26394c-c429-4268-a489-d179da0314e5" />
3. Jika tidak memilih kategori menu pilihan (kosong) <br>
<img width="353" height="89" alt="image" src="https://github.com/user-attachments/assets/d9a3aa40-b331-4d24-8c43-db4a42f03958" />

























   
