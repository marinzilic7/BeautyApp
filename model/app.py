from __init__ import Session

from proizvodi import Proizvod
from korisnici import Korisnik
from __init__ import Base
from datetime import datetime
from sqlalchemy.exc import IntegrityError





import os 
from flask import Flask,render_template, request,redirect, url_for,flash,session



app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))
app.secret_key = 'ovo-je-moj-tajni-kljuc'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/")
def index ():
    return render_template('register.html') 


@app.route('/register', methods=['POST'])
def register_user():
    
    ime = request.form['ime']
    prezime = request.form['prezime']
    email = request.form['email']
    password = request.form['lozinka']
    
    korisnik = Korisnik(ime=ime, prezime=prezime, email=email, password=password)
    Session.add(korisnik)
    Session.commit()

    flash('Uspjesna registracija ', 'success')
    return redirect(url_for('login'))


@app.route("/login")
def login ():
    return render_template('login.html')

@app.route('/loguser', methods=['GET', 'POST'])
def log_user():
   
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = Session.query(Korisnik).filter_by(email=email, password=password).first()
       
        if user:
            session['user_name'] = user.ime
            session['user_id'] = user.ID_korisnika
           
            return redirect(url_for('home'))
        else:
            flash('Pogrešan e-mail ili lozinka. Molimo pokušajte ponovno.', 'danger')
            return redirect(url_for('login'))

@app.route("/pocetna")
def home ():
    return render_template('pocetna.html')

@app.route('/logout')
def logout():
    
    session.pop('user_name', None)
   
    return redirect(url_for('login'))


@app.route("/proizvodi")
def proizvod ():
    proizvod = Session.query(Proizvod).all()
    return render_template('proizvod.html', proizvodi=proizvod)

@app.route('/dodaj-proizvod', methods=['POST'])
def dodaj_proizvod():
    
    ime = request.form['ime']
    opis = request.form['opis']
    cijena = request.form['cijena']
   
    
    proizvod= Proizvod(ime=ime, opis=opis, cijena=cijena,)
    Session.add(proizvod)
    Session.commit()
    return redirect(url_for('proizvod'))


@app.route('/izbrisi_proizvod/<int:ID_proizvoda>', methods=['POST'])
def izbrisi_proizvod(ID_proizvoda):
    proizvod = Session.query(Proizvod).get(ID_proizvoda)
    
    Session.delete(proizvod)
    Session.commit()  
        
    return redirect(url_for('proizvod'))
    
        
    
@app.route('/uredi_proizvod/<int:ID_proizvoda>')
def uredi_proizvod(ID_proizvoda):
    proizvod = Session.query(Proizvod).get(ID_proizvoda)
    
    return render_template('uredi_proizvod.html', proizvod=proizvod) 

@app.route('/update_proizvod/<int:ID_proizvoda>', methods=['POST'])
def update_proizvod(ID_proizvoda):
    proizvod = Session.query(Proizvod).get(ID_proizvoda)
    if proizvod:
        
        proizvod.ime = request.form.get('ime')
        proizvod.opis = request.form.get('opis')
        proizvod.cijena = request.form.get('cijena')
      
        Session.commit()
  
    return redirect(url_for('proizvod'))


app.debug = True

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=5000)