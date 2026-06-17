from flask import Flask, request
app = Flask(__name__)
 
@app.route('/')
def index():
    return "Hello World"
    #also it could be changed into html - return "<h1>hello world</h1>"

@app.route('/abc')
def hello():
    return "hehe"

@app.route('/greet/<name>')
def greet(name):
    return f"helloo {name}"

@app.route('/add/<number1>/<number2>')
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"


#@app.route('/handle_url_params')
#def handle_params():
 #   return str(request.args)
#http://127.0.0.1:5555//handle_url_params?name=Rekhss&greeting=Helloo
# output - ImmutableMultiDict([('name', 'Rekhss'), ('greeting', 'Helloo')])

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f"{greeting}, {name}"
    else:
        return 'some parameters are missing'
    
# url - http://127.0.0.1:5555/handle_url_params?greeting=Hello&name=Rekhss
# output - Hello, Rekhss

@app.route('/greet_params')
def greet_params():
    greeting = request.args.get('greeting')
    name = request.args.get('name')
    return f"{greeting}, {name}"

#to consider this concatenated string as actual numerical calculation - @app.route('/add/<int:number1>/<int:number2>') (typecasting)
if __name__ == '__main__': 
    app.run(host='0.0.0.0',port = 5555, debug = True)


