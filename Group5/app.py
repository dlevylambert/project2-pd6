from flask import Flask
from flask import request
from flask import render_template
from flask import url_for,redirect,flash
from flask import session, escape
import util, urllib2,json

app = Flask(__name__)

gamelist = []
imagelist = []
descriptionlist = []

@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template('home.html')
	else:
		button = request.form['button']
		if button == 'Search':
			global gamelist
			global imagelist
			gamelist= util.search(request.form['textarea'],0)['names']
			images = util.search(request.form['textarea'],0)['images']
			descriptions = util.search(request.form['textarea'],0)['descriptions']
			imagelist = []
			for i in range(len(images)):
				imagelist.append(images[i]['super_url'])
			print descriptions[0]
			return redirect(url_for('results'))
		

@app.route("/results", methods=['GET', 'POST'])
def results():
	#global gamelist
	if request.method == 'GET':
		

		return render_template('results.html', gamelist=gamelist, imagelist=imagelist)

if __name__=="__main__":
    app.debug=True # remove this line to turn off debugging
    app.run()


