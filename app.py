from flask import Flask, render_template, url_for, redirect
app = Flask(__name__, template_folder='templates')

@app.route(rule: '/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
       return render_template('index.html')
     else request.method == 'POST':
       username = request.form.get('username')
       password = request.form.get('password')

       if username == 'rekha' and password == 'poorna':
           return 'Success'
       else:
           return 'Failure'
           
 

if __name__ == '__main__': 
    app.run(host='0.0.0.0',port = 5555, debug = True)

