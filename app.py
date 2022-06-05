from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/', methods =["GET", "POST"])
def getRandomJoke():
    if request.method == "POST":
        numJokes = int(request.form.get("numJokes"))
        address = "https://icanhazdadjoke.com/"
        data = {"Accept": "application/json"}
        jokes = []
        for i in range(numJokes):
            resp = requests.get(address, headers=data)
            jokes.append(resp.json()["joke"])
        return render_template('index.html', jokes=jokes, numJokes=numJokes)
    return render_template('index.html', numJokes=1)

if __name__ == "__main__":
    app.run(debug=True)