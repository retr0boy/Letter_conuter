from app import app
from flask import render_template, redirect
from app.forms import MyForm
from werkzeug.utils import secure_filename
import os
import secrets
from chardet.universaldetector import UniversalDetector
from mylib import count_ru_letters, detect_encoding


@app.route('/')
@app.route('/index')
def hello():
    countries = {'Rusea':'moskorowa','washdc':'usausa','kaza':'asta'}
    return render_template('index.html', data = countries)


@app.route('/upload', methods=['GET', 'POST'])
@app.route('/upload', methods=['GET', 'POST'])
def upload():

    form = MyForm()
    if form.validate_onsubmit ():

        , file_ext = os.path.splitext(form.file.data.filename)
        files_dir=os.path.join(os.getcwd(), 'files')
        filename=os.path.join(files_dir, secrets.token_hex(nbytes=16)+file_ext)
        if 'files' not in os.listdir(os.getcwd()):
            os.mkdir(files_dir)
        form.file.data.save(filename)
        f = open(filename, "r", encoding=detect_encoding(filename)['encoding'])
        text=f.read()
        count_ru_letters(text)
        return render_template('index.html',title = form.name.data, text=text)
    return render_template('upload.html', form=form)