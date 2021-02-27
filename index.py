from flask import Flask
from flask import render_template,request 


app = Flask(__name__)


@app.route("/")
@app.route("/index")

def index():
    return "Merhaba  Blog ziyaretçileri!"
	
@app.route("/contact")
def contact():
    return "Burası bizim iletişim sayfamız"

@app.route("/about")
def about():
   
   id = 3
   return render_template("about.html", sayfabasligi="bizim sayfamız", sayfaid = id)
	
@app.route('/yazar/<string:id>')
def yazar(id):
   return "Kitap ID si:" + id
   
# Hizmetler Sayfası
@app.route('/hizmetler')
def hizmetler():
   return render_template("hizmetler.html")
   
# Bebek Bakıcılığı Sayfası
@app.route('/baby-care')
def bebekbakiciligi():
   return render_template("baby-care.html")
   
# If Else Koşullar
@app.route('/ifelse')
def ifelse():
   return render_template("ifelse.html", toplam = toplamf(1,6))
   
def toplamf(a,b):
	return a+b
	
# For While Döngüler
@app.route('/donguler')
def donguler():
   sehirler = ["İstanbul","Ankara","İzmir","Kayseri"]
   return render_template("donguler.html", sehirler=sehirler)
   
# Form Sayfası
@app.route('/mesajyazin')
def mesajyazin():
   return render_template("form.html")
   
# Form Verileri Alma
@app.route('/verilerial', methods=['POST', 'GET'])
def verilerial():
   if request.method == 'POST':
      isim = request.form.get('isim') 
      mesaj = request.form.get('mesaj')

      return render_template("verilerigoster.html",isim=isim,mesaj=mesaj)

   else:
      return render_template("verilerigoster.html",hata="Formdan veri gelmedi!")
	
if __name__ == "__main__":
    app.run(debug=True)
