from flask import Flask, request, make_response
app = Flask(__name__)
 
@app.route('/')
def index():
    return "Hello World"
    #also it could be changed into html - return "<h1>hello world</h1>"

@app.route('/abc')
def hello():
        response = make_response('hehehheee\n')
        response.status_code = 202
        response.headers['content-type'] = 'application/octet-stream'
        return response

@app.route('/greet/<name>')
def greet(name):
    return f"helloo {name}"

@app.route('/add/<number1>/<number2>')
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"



@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f"{greeting}, {name}"
    else:
        return 'some parameters are missing'
    

@app.route('/greet_params')
def greet_params():
    greeting = request.args.get('greeting')
    name = request.args.get('name')
    return f"{greeting}, {name}"

#to consider this concatenated string as actual numerical calculation - @app.route('/add/<int:number1>/<int:number2>') (typecasting)
if __name__ == '__main__': 
    app.run(host='0.0.0.0',port = 5555, debug = True)


#------------------------------------------------------------------------
#Browser:  http://127.0.0.1:5555/
#Output:  Hello World

#Browser:  http://127.0.0.1:5555/abc
#Output:  hehe

#Browser:  http://127.0.0.1:5555/greet/Rekhss
#Output: helloo Rekhss

#Browser: http://127.0.0.1:5555/handle_url_params?greeting=Hello&name=Rekhss
#Output:Hello, Rekhss