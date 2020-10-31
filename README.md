# LatihanVCS
Tugas bahasa pemrograman

Nama    : Asri Liya Astuti

NIM     : 312010104

Kelas   : TI.20.B.1

Dosen   : Agung Nugroho, S.Kom, M.Kom


##Jika Git sudah terinstal di Windows. Untuk mencobanya, silahkan buka CMD atau PowerShell, kemudian ketik perintah.

  $ git --version
  
 ![Screenshot (15)](https://user-images.githubusercontent.com/72993076/97783006-79276980-1bc7-11eb-89c4-391bfeaa44ee.png)

##Config global repository

$ git config --global user.name “nama_user”

$ git config --global user.email “nama_user”

	
        	



#PERINTAH DASAR GIT

1.	git init, perintah untuk membuat repository local.
2.	git add, perintah untuk menambahkan file baru, atau perubahan pada file pada staging sebelum proses commit.
3.	git commit, perintah untuk menyimpan perubahan kedalam database git.
4.	git push -u origin master, perintah untuk mengirim perubahan pada repository local menuju server repository.
5.	git clone [url], perintah untuk membuat working directory yang diambil dari repositry sever.
6.	git remote add origin [url], perintah untuk menambahkan remote server/reopsitory server pada local repositry (working directory).
7.	git pull, perintah untuk mengambil/mendownload perubahan terbaru dari server repository ke local repository.
	


#TUTORIAL PENGGUNAAN GIT

1.	Buat folder terlebih dahulu di Windows Explorer.
2.	Untuk penggunaan git pertama masuk ke folder yang akan digunakan. Klik kanan dan pilih Git Bash.
Buat direktory project praktikum pertama.
          
3.	Setelah itu, jalankan perintah git init, untuk membuat repository local.

       ![Screenshot (34)](https://user-images.githubusercontent.com/72993076/97783159-7ed17f00-1bc8-11eb-88fc-e6fe7fc7e707.png)



4.	Buat satu file bernama README.md.

        $ echo “# Latihan1” >> README.md

        File README.md berhasil dibuat.
	
     ![Screenshot (35)](https://user-images.githubusercontent.com/72993076/97783192-b50efe80-1bc8-11eb-904b-65da5e0002a9.png)   
	


5.	Untuk menambahkan file yang baru saja dibuat tersebut gunakan perintah git add.

        $ git add README.md

	File README.md berhasil ditambahkan.
  
	![Screenshot (35)](https://user-images.githubusercontent.com/72993076/97783192-b50efe80-1bc8-11eb-904b-65da5e0002a9.png)
       
             
6.	Untuk menyimpan perubahan yang ada kedalam database repository local, gunakan perintah 
git commit -m “komentar commit”.

        $ git commit -m “File pertama saya”
	
	![Screenshot (35)](https://user-images.githubusercontent.com/72993076/97783192-b50efe80-1bc8-11eb-904b-65da5e0002a9.png)


7.	Untuk menambahkan remote repository server, gunakan perintah git remote add origin [url].

        $ git remote add origin https://github.com/asriliya/asriliyaa.git
	
	
	![Screenshot (35)](https://user-images.githubusercontent.com/72993076/97783192-b50efe80-1bc8-11eb-904b-65da5e0002a9.png)





8.	Untuk mengirim perubahan pada local repository ke server gunakan perintah git push.

        $ git push -u origin master

	Perintah ini akan meminta memasukkan username dan password pada akun github.com
	
	
	![Screenshot (36)](https://user-images.githubusercontent.com/72993076/97783270-2babfc00-1bc9-11eb-99ae-ef036566c26c.png)


	 
	 
 #Melihat hasilnya pada server repository
 
•	Buka laman github.com, arahkan pada repositorinya.

•	Maka perubahan akan terlihat pada laman tersebut.
![Screenshot (38)](https://user-images.githubusercontent.com/72993076/97783372-d0c6d480-1bc9-11eb-98a7-9e642174264a.png)




9.	Clone repository, pada dasarnya adalah meng-copy repository server dan secara otomatis membuat satu direktory sesuai dengan nama repositorynya (working directory).
Untuk melakukan cloning, gunakan perintah git clone [url].



