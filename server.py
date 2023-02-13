from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "anything you want"
@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = 1
    else:
        session['number']+=1    
    return(render_template("index.html"))

@app.route('/index3')
def index3():
    if 'number' not in session:
        session['number'] = 1
    else:
        session['number'] +=1
    return redirect('/')

@app.route('/index4')
def index4():
    session.clear()
    return redirect('/')

@app.route('/index2', methods=['POST'])
def index2():
    return(render_template("index2.html"))



if __name__=="__main__":
    app.run(debug=True)