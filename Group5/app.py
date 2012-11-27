from flask import *
import util

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template('home.html')

if __name__=="__main__":
    app.debug=True # remove this line to turn off debugging
    app.run()
