from flask import Flask, render_template, session, url_for, request, escape, redirect, jsonify
import POC, trie
import string

#configuration
DEBUG = True

#init
app = Flask(__name__)
app.config.from_object(__name__)
ptree = trie.Prefix_Tree()
ptree.add_words([word.rstrip("\n") for word in open("sowpods.txt")])

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
    return s/len(words)

def percent_correct(words):
    count = 0
    for word in words:
        if word in ptree:
            count += 1
    return count / len(words) * 100

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/get_data")
def get_data():
    c_name = request.args.get("name")
    celeb = POC.get_celeb(c_name)
    tweets = [tweet["text"] for tweet in POC.get_tweets(celeb["screen_name"])]
    words = filter(lambda x: len(x) and not ignore(x), [word for word in tweet.split(" ") for tweet in tweets])
    words = map(lambda x: x.translate(string.maketrans("",""), string.punctuation).lower(), words)
    res = {"Total Words": len(words),
            "Average Word Length": get_average_word_length(words),
            "Percentage Of Words Spelled Correctly": percent_corrent(words)}
    return jsonify(res)

if __name__ == "__main__":
    app.run()
