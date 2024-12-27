from flask import Flask, render_template

app = Flask(__name__)

# Rute untuk halaman beranda
@app.route('/')
def beranda():
    return render_template('web.html')  # Mengarahkan ke template web.html

# Rute untuk halaman tentang Covid
@app.route('/tentang_covid')
def tentang_covid():
    return render_template('tentang_covid.html')  # Mengarahkan ke template tentang_covid.html

# Rute untuk halaman simulasi Monte Carlo
@app.route('/simulasi')
def simulasi():
    return render_template('simulasi.html')  # Mengarahkan ke template simulasi.html

if __name__ == '__main__':
    app.run(debug=True)