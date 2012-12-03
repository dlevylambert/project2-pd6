from flask import Flask
from flask import request
from flask import render_template
from flask import url_for,redirect,flash
from flask import session, escape
import util, urllib2,json

app = Flask(__name__)

gamelist = []
imagelist = []
description = ""

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
			imagelist = []
			for i in range(len(images)):
				try:
					imagelist.append(images[i]['super_url'])
				except TypeError:
					imagelist.append("http://www.worldofchemicals.com/Woclite/tmp/chem/no_image.gif")
			return redirect(url_for('results'))
		

@app.route("/results", methods=['GET', 'POST'])
def results():
	global description
	if request.method == 'GET':
		return render_template('results.html', gamelist=gamelist, imagelist=imagelist)
	else:
		button = request.form['button']
		print button
		description = util.search(button,0)['descriptions'][0]
		print description
		return redirect(url_for('description', description=description))

@app.route("/description", methods=['GET', 'POST'])
def description():
	if request.method == 'GET':
		return render_template('descript.html', description=description)





if __name__=="__main__":
    app.debug=True # remove this line to turn off debugging
    app.run()





















