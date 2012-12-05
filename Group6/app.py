from flask import Flask, render_template, session, url_for, request, escape, redirect, jsonify
import traceback
import POC, trie
import string

#configuration
DEBUG = True

#init
app = Flask(__name__)
app.config.from_object(__name__)
ptree = trie.Prefix_Tree()
with open("sowpods.txt", "r") as f:
    ptree.add_words([word.rstrip() for word in f])

def ignore(word):
    l = ["#", "@", "http"]
    for c in l:
        if c in word:
            return True
    return False

def get_average_word_length(words):
    s = 0
    for word in words:
        s += len(word)
    return float(s) / len(words)

def percent_correct(words):
    count = 0
    for word in words:
        if word in ptree:
            count += 1
    return float(count) / len(words) * 100

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/get_data")
def get_data():
    c_name = request.args.get("name")
    celeb = POC.get_celeb(c_name)
    tweets = [tweet["text"] for tweet in POC.get_tweets(celeb["screen_name"])]
    words = []
    for tweet in tweets:
        tweet = tweet.encode('ascii', 'ignore')
        try:
            for w in tweet.split(" "):
                if not ignore(w):
                    w = w.translate(string.maketrans("",""), string.punctuation).lower()
                    if w:
                        words.append(w)
        except Exception: 
            traceback.print_exc() 
    res = {"Total Words": len(words),
            "Average Word Length": get_average_word_length(words),
            "Percentage Of Words Spelled Correctly": percent_correct(words)}
    return jsonify(res)

if __name__ == "__main__":
    app.run()
