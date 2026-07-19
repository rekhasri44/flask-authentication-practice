import pandas as pd
from flask import Flask, render_template, url_for, redirect
app = Flask(__name__, template_folder='templates')

@app.route(rule: '/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
       return render_template('index.html')
     else request.method == 'POST':
       username = request.form.get("username")
       password = request.form.get("password")

       if username == 'rekha_kprs" and password == "poorna":
          return 'success'
       else:
          return 'failure'

@app.route('/file_upload', methods=["POST"])
def file_upload():
    file = request.files('file")

    if file.content_type == 'text/plain':
                         return file.read().decode()
    elif file.content_type == 'application/vmd.openxmlformats-officedocument.spreadsheetml.sheet or file.content_type == 'application/vmd.ms-excel, text/plain'
                         df = odf.read_excel(file)
                         return df.to_html()

if __name__ == '__main__': 
    app.run(host='0.0.0.0',port = 5555, debug = True)

