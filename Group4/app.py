from flask import Flask,render_template,request,url_for,redirect,session
import util

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
        if request.form.has_key('login'):
            user = str(request.form['user'])
            password = str(request.form['pass'])
            if user in util.getUsernames():
                if password == util.checkPassword(user):
                    session['user'] = user
                    return redirect(url_for('menu'))
            return render_template('login2.html')
        if request.form.has_key('newuser'):
            return redirect(url_for('newuser'))

@app.route('/newuser/',methods=['GET','POST'])
def newuser():
    if request.method=='GET':
        return render_template('newuser.html',notmatching=False,taken=False)
    else: 
        if request.form.has_key('submit'):
            user = request.form['user']
            password1 = request.form['pass1']
            password2 = request.form['pass2']
            number = request.form['num']
            if user in util.getUsernames():
                return render_template('newuser.html',notmatching=False,taken=True)
            if password1 != password2:
                return render_template('newuser.html',notmatching=True,taken=False)
            util.createNewUser(user,password1,number)
            return redirect(url_for('login'))
            
@app.route('/menu/',methods=['GET','POST'])
def menu():
    return render_template('menu.html')
if __name__ == "__main__":
    app.debug = True 
    app.run(host='0.0.0.0', port=6004)
    
