from flask import Flask, render_template, session, url_for, request, escape, redirect, jsonify
import POC

#configuration
DEBUG = True

#init
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/get_data")
def get_data():
    c_name = request.args.get("name")
    celeb = POC.get_celeb(c_name)
    res = {"tweets": []}
    if celeb:
        res["tweets"] = [tweet["text"] for tweet in POC.get_tweets(celeb["screen_name"])]
    return jsonify(res)
        

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
