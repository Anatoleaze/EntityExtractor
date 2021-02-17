from flask import Flask, render_template, request, flash, redirect
from app.program import Work
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/text')
def text():
    return render_template("formulaire.html")

@app.route('/resultats', methods=('GET', 'POST'))
def resultats():
    prog=Work()
    if "texte" in request.form.keys():
      prog.getContentFreeTxt(request.form["texte"])
    elif "url" in request.form.keys():
        prog.getContentURL(request.form["url"])
    else:
         if 'file' in request.files:
            file = request.files['file']
            if file and file.filename != '':
                file.save(os.path.join(file.filename))
            #prog.getContentFile(file.filename)
    html=""#prog.analyseText()
    return render_template("resultat.html", recap=prog.getTypesEntity(html),texte=html)