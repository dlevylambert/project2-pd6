from flask import Flask,render_template,request,url_for,redirect,flask,session

app = Flask(__name__)
app.secret_key = 'superduperkeyofsecretness'

@app.route('/')
def start():
    return redirect(url_for('test'))

@app.route('/test/',methods=['GET','POST'])
def test():
    
