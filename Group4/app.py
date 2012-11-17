from flask import Flask,render_template,request,url_for,redirect,session

app = Flask(__name__)
app.secret_key = 'superduperkeyofsecretness'

@app.route('/')
def start():
    return redirect(url_for('login'))

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login1.html')
    else:
        if request.form['login']=='Login':
            user = str(request.form['user'])
            password = str(request.form['pass'])
            userdata = file('users.txt')
            for line in userdata:
                data = line.split(',')
                if user == data[0].strip():
                    if password == data[1].strip():
                        session['user'] = user
                        return redirect(url_for('menu'))
                    else:
                        break
            return render_template('login2.html')
            
if __name__ == "__main__":
    app.debug = True 
    app.run(host="nathaniel.biggs@ml7.stuycs.org",port=6004)
    
