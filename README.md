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

**Virtual Environment (venv)** adalah lingkungan isolasi mandiri yang dibuat khusus untuk sebuah proyek Python. Di dalamnya, Anda bisa menginstal pustaka (library) atau paket Python dengan versi tertentu tanpa mengganggu pengaturan Python global atau proyek lainnya pada komputer yang sama.

**Mengapa ini penting?**
Bayangkan Anda mengerjakan Proyek A yang membutuhkan **Flask 1.0**, tetapi di saat bersamaan Anda juga mengerjakan Proyek B yang mewajibkan **Flask 2.0**. Tanpa venv, kedua versi ini akan bentrok. Dengan venv, setiap proyek memiliki "ruang kerja" sendiri sehingga dependensi antar proyek tidak saling mengganggu.

## Instalasi dan Setup Virtual Environment
### Instalasi venv
Buka terminal atau Command Prompt (CMD), arahkan ke folder proyek Anda, lalu jalankan perintah berikut:
```sh
# Windows
python -m venv venv

# macOS / Linux
python3 -m venv venv
```

### Setup venv
Setelah berhasil dibuat, Anda perlu mengaktifkan lingkungan tersebut agar sistem tahu bahwa Anda sedang bekerja di dalamnya:
```sh
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

Jika berhasil masuk, tampilan terminal Anda akan diawali dengan tanda kurung nama environment, seperti ini:
```sh
(venv) C:\Coding\magang>
```
## Apa Itu Flask?

**Flask** adalah micro-framework web berbasis Python yang ringan, fleksibel, dan sangat ideal untuk membangun aplikasi web maupun API. Flask populer karena penggunaannya yang sederhana (minimalis) namun didukung oleh komunitas yang sangat besar. Ini menjadikannya pilihan tepat bagi developer pemula maupun profesional.

Untuk menginstal Flask di dalam virtual environment, gunakan perintah:
```sh
pip install Flask
```

### Setup Flask
Langkah pertama adalah mendefinisikan aplikasi Flask Anda dengan membuat instance dari kelas Flask.
```py
from flask import Flask

app = Flask(__name__)
```

### Route dan Fungsi
Route (rute) berfungsi untuk memetakan URL ke fungsi Python tertentu. Jadi, ketika pengguna mengakses URL tertentu, Flask akan menjalankan fungsi yang sesuai.

#### Return HTML 
Contoh paling sederhana adalah mengembalikan teks atau HTML langsung ke browser.
```py
@app.route('/')
def index():
  return "<h1>Selamat Datang di API Saya!</h1>"
```
Penjelasan: Ketika pengguna mengakses halaman utama (/), fungsi index akan dijalankan dan teks "Selamat Datang di API Saya!" akan dikirim kembali ke pengguna.

#### Return File
Untuk menampilkan halaman web utuh, kita biasanya menggunakan file HTML terpisah.
```py
from flask import render_template

@app.route('/')
def index():
    pesan = "Hello World"
    # Mengirimkan variabel 'pesan' agar bisa dibaca di dalam home.html
    return render_template("home.html", temp=pesan)
```
Penjelasan: Fungsi ini akan me-render file home.html yang ada di folder templates dan menyisipkan data variabel pesan ke dalamnya.

#### Return Json (response)
Jika Anda membuat API, data biasanya dikirim dalam format JSON.
```py
from flask import jsonify

@app.route('/data')
def get_data():
    data = {
        'nama': 'Rimuru',
        'nrp': 5025241043,
        'jurusan': 'Teknik Informatika'
    }
    # Mengembalikan data JSON dengan status code 200 (Sukses)
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
        # Menangkap data dari form
        judul = request.form.get('judul')
        author = request.form.get('author')
        rilis = request.form.get('rilis')
        
        # Menyimpan data ke list sementara
        koleksi.append({'judul': judul, 'author': author, 'rilis': rilis})
        return redirect('/')
    else:
        # Jika method GET, kembalikan ke halaman awal (atau tampilkan form)
        return redirect('/')
```


## Referensi:
https://flask.palletsprojects.com/en/stable/quickstart/
<br>
https://www.codepolitan.com/blog/apa-itu-flask-panduan-membangun-api-dengan-flask/
https://belajarpython.com/tutorial/virtual-environment-python/