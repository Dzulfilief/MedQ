from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
import db

app = Flask(__name__)
db.init_db()


@app.route("/", methods=["GET", "POST"])
def index():
    hasil = []
    estimasi_selesai = ""
    now = datetime.now().strftime("%H:%M")

    if request.method == "POST":
        durasi = int(request.form["durasi"])
        jam_mulai = request.form["mulai"] or "08:00"
        jumlah_dokter = int(request.form["dokter"])

        # Ambil jumlah pasien per poli
        poli_list = {
            "Poli Umum": int(request.form.get("umum", 0)),
            "Poli Gigi": int(request.form.get("gigi", 0)),
            "Poli Anak": int(request.form.get("anak", 0)),
        }

        db.clear_antrian()
        no_urut = 1  # Nomor pasien keseluruhan

        for nama_poli, jumlah_pasien in poli_list.items():
            if jumlah_pasien == 0:
                continue

            waktu_dokter = [datetime.strptime(jam_mulai, "%H:%M")] * jumlah_dokter

            for i in range(jumlah_pasien):
                dokter_ke = i % jumlah_dokter
                mulai = waktu_dokter[dokter_ke]
                selesai = mulai + timedelta(minutes=durasi)

                status = (
                    "Diperiksa"
                    if mulai.strftime("%H:%M") == jam_mulai
                    else "Dalam Antrean"
                )
                dokter = f"{nama_poli} - Dokter {chr(65 + dokter_ke)}"

                db.insert_pasien(
                    no=no_urut,
                    mulai=mulai.strftime("%H:%M"),
                    selesai=selesai.strftime("%H:%M"),
                    status=status,
                    dokter=dokter,
                    poli=nama_poli,
                )

                waktu_dokter[dokter_ke] = selesai
                no_urut += 1

            # Simpan riwayat per poli
            db.insert_riwayat(jumlah_pasien, jumlah_dokter, durasi, nama_poli)

    hasil = db.get_antrian()
    estimasi_selesai = hasil[-1]["selesai"] if hasil else ""

    return render_template(
        "index.html",
        hasil=hasil,
        poli="Semua Poli",
        now=now,
        selesai=estimasi_selesai,
    )


@app.route("/reset", methods=["POST"])
def reset():
    db.clear_antrian()
    return redirect(url_for("index"))


@app.route("/riwayat")
def riwayat():
    data = db.get_riwayat()
    return render_template("riwayat.html", data=data)


@app.route("/cetak")
def cetak():
    hasil = db.get_antrian()
    poli = hasil[0]["poli"] if hasil else ""
    return render_template("cetak.html", hasil=hasil, poli=poli)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
