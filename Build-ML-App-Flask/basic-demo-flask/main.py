from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Welcome to Flask Application!</h1>"

@app.route("/welcome")
def welcome():
    return "<h2>Welcome navigation</h2>"

@app.route("/welcome/<user>")
def welcome_user(user):
    return f"<h2>Welcome {user} to Flask Application</h2>"

@app.route('/square', methods=['GET'])
def squarenumber():
    if request.method == 'GET':
        if(request.args.get('num') == None): # when user requests first time, it will be None
            return render_template('square.html')
        elif(request.args.get('num') == ''):
            return "<html><body> <h1>Invalid input</h1></body></html>"
        else:
            number = request.args.get('num')
            sqare = int(number) * int(number)
            return render_template('solution.html',
                                   squareofnum=sqare, num=number)


if __name__=="__main__":
    app.run()