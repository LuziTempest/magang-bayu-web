from flask import Flask, render_template, jsonify, request, redirect
app = Flask(__name__)

perpustakaan = [
    {"kode": "PBW01", "judul": "Jago Coding Dalam Sekejab", "pengarang": "Leley"},
    {"kode": "JKW02", "judul": "77 Keajaiban Jombang", "pengarang": "Sanby"}
]

@app.route("/")
def home():
    global perpustakaan
    return render_template("home.html", perpustakaan=perpustakaan)

@app.route("/add", methods=["GET", "POST"])
def add():
    global perpustakaan
    if request.method == "POST":
        kode = request.form.get('kode')
        judul = request.form.get('judul')
        pengarang = request.form.get('pengarang')
        data_baru = {'kode': kode, 'judul': judul, 'pengarang': pengarang}
        perpustakaan.append(data_baru)
        return redirect("/")
    else: 
        return "Tidak bisa langsung url mas"

@app.route("/delete/<string:kode>")
def delete(kode):
    global perpustakaan
    perpustakaan = [item for item in perpustakaan if item['kode'] != kode]
    return redirect("/") 

@app.route("/tampilkan_data")
def data():
    global perpustakaan
    return jsonify(perpustakaan), 200

app.run(debug=True)