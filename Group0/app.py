from flask import Flask
from flask import url_for,redirect, flash
from flask import session, escape
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def homepage():
        if request.method == "GET":
		return render_template("musicboxhome.html");
        else:
		button = request.form["button"]
		if button == 'Home':
			return redirect(url_for('moviechooser'))
		if button == 'About Us':
			return redirect(url_for('aboutus'))
		
@app.route("/aboutus.html",methods=["GET"])
def aboutus():
	return render_template("aboutus.html")

#will add search later

if __name__ == "__main__":
    app.debug = True
    app.run();
