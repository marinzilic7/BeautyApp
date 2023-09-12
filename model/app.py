from __init__ import Session


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


app.debug = True

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=5000)