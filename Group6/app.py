from flask import Flask, render_template, session, url_for, request, escape, redirect, jsonify
import POC, trie
from pytrie import SortedStringTrie as trie

#configuration
DEBUG = True

#init
app = Flask(__name__)
app.config.from_object(__name__)
ptree = Prefix_Tree()
@app.route("/get_data")
def get_data():
    c_name = request.args.get("name")
    celeb = POC.get_celeb(c_name)
    res = {"tweets": []}
    if celeb:
        res["tweets"] = [tweet["text"] for tweet in POC.get_tweets(celeb["screen_name"])]
    return res

def get_averagewordcount(data):
    words = []
    counts = []
    for i in data:
        words = i.split()
        wordc = len(words)
        counts.append(wordc)
    average = sum(counts)/len(counts)
    return average

def countTotalWords(data): #data should be a txt file!
    totalWords = 0
    f = file.open(data)
    for word in f:
        word.replace(".", "")
        word.replace("@", "")
        word.replace("'", "")
        word.replace("#", "")
        word.replace(",", "")
        word.lower()
        totalWords++
    return totalWords

def godFunction():    
    with open("sowpods.txt") as f:
        for line in f:
            ptree.add(f.strip("\n"))

def countCorrectWords():
    totalWords = countTotalWords("res.txt")
    correctWords = 0
    with open("res.txt") as f:
        for line in f:
            if line in ptree:
                correctWords++
    return ((correctWords/totalWords) * 100) + "% words spelled correctly"
                
        
def send_data():
    return jsonify(get_data())

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()