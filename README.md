# Modul Magang Web Development TD

- [Modul Magang Web Development TD](#modul-pengenalan-gns3)
  - [Apa Itu Virtual Environment?](#apa-itu-virtual-environment?)
  - [Instalasi dan Setup Virtual Environment](#instalasi-dan-setup-virtual-environment)
    - [Instalasi venv](#instalasi-venv)
    - [Setup venv](#setup-venv)
  - [Apa Itu Flask?](#apa-itu-flask?)
    - [Instalasi Flask](#instalasi-flask)
    - [Route dan Fungsi](#route-dan-fungsi)
        - [Return HTML](#return-html)
        - [Return File](#return-file)
        - [Return Json](#return-json)
    - [Methods](#methods)
  - [Referensi](#referensi)

## Apa Itu Virtual Environment?

**Virtual Environment (venv)** Virtual environment adalah lingkungan terisolasi yang dibuat untuk proyek Python tertentu. Di dalamnya, kamu bisa menginstall versi paket Python tanpa mengganggu pengaturan sistem Python atau proyek lainnya.

Misalnya, kamu sedang mengerjakan proyek dengan Flask 1.0.2, tapi di waktu yang sama kamu juga perlu menggunakan Flask 1.1.2 untuk proyek lain. Dengan ini, kamu bisa mengatur kedua proyek ini tanpa bentrok, karena masing-masing proyek punya "lingkungan" paketnya sendiri.

## Instalasi dan Setup Virtual Environment
### Instalasi venv
Buka terminal atau command prompt di direktori proyek Anda, lalu jalankan:
```sh
# Windows
python -m venv venv

# macOS / Linux
python3 -m venv venv
```

### Setup venv
Setelah dibuat, Anda harus mengaktifkannya:
```sh
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

Jika sudah masuk ke dalam virtual enviropment akan muncul tanda berikut
```sh
(venv) C:\Coding\magang>
```
## Apa Itu Flask?

**Flask** adalah framework web Python yang simpel, fleksibel, dan ideal untuk membangun API yang ringan dan efisien. Fungsi Flask yaitu memudahkan penggunaan dan komunitas yang aktif. Sehingga Flask di katakan menjadi pilihan yang tepat bagi developer Python yang ingin memulai pengembangan API.
Untuk menginstal Flask ke dalam lingkungan Python Anda. Ini dapat di lakukan menggunakan pip:
```sh
pip install Flask
```
### Setup Flask
Pertama kali definisikan aplikasi Flask Anda. Ini dilakukan dengan membuat instance dari class Flask.
```py
from flask import Flask

app = Flask(__name__)
```

### Route dan Fungsi
Route (rute) menentukan URL yang akan di proses oleh aplikasi Flask Anda. Untuk setiap route, Anda perlu mendefinisikan fungsi yang akan menangani permintaan yang masuk.

#### Return HTML 
```py
@app.route('/')
def index():
  return "<h1>Selamat Datang di API Saya!</h1>"
```
Di contoh kode tersebut, route "/" akan diproses oleh fungsi index. Fungsi index kemudian mengembalikan string "Selamat Datang di API Saya!" yang akan dikirimkan sebagai response kepada pengguna.

#### Return File
```py
@app.route('/')
def index():
  temp = "Hello word"
  return render_template("home.html", temp=temp)
```
Fungsi index diatas akan menampilkan file home.html dan mengirimkan variabel temp.

#### Return Json (response)
```py
@app.route('/data')
def get_data():
  data = {
    'nama': 'Rimuru',
    'nrp': 5025241043,
    'jurusan': 'Teknik Informatika'
  }
  return jsonify(data), 200
```
Fungsi get_data akan mengembalikan data pengguna dalam format JSON dengan status code 200 (OK). Method jsonify digunakan untuk mengonversi data Python menjadi format JSON yang dapat di baca oleh client.

### Methods
HTTP method menentukan jenis request (permintaan) yang di kirimkan oleh client (pengguna) ke server (aplikasi Anda). Beberapa HTTP method yang umum di gunakan dalam pengembangan API adalah:
- GET: Digunakan untuk mengambil data dari server.
- POST: Digunakan untuk mengirim data baru ke server.
- PUT: Digunakan untuk memperbarui data yang sudah ada di server.
- DELETE: Digunakan untuk menghapus data dari server.
```py
@app.route('/add', methods=["GET", "POST"])
def tambah():
    if request.method == "POST":
        judul = request.form.get('judul')
        author = request.form.get('author')
        rilis = request.form.get('rilis')
        koleksi.append({'judul': judul, 'author': author 'rilis': rilis})
        return redirect('/')
    else:
        return redirect('/')
```


## Referensi:
https://flask.palletsprojects.com/en/stable/quickstart/
<br>
https://www.codepolitan.com/blog/apa-itu-flask-panduan-membangun-api-dengan-flask/
https://belajarpython.com/tutorial/virtual-environment-python/