from flask import Flask, render_template, request
import requests

app = Flask(__name__)
GIPHY_API_KEY = "DwaNDxUz8wmKHkQfWxXInCcHvzE8Yden"

@app.route("/", methods=["GET", "POST"])
def home():
    gifs = []
    if request.method == "POST":
        termo = request.form["termo"]
        url = "https://api.giphy.com/v1/gifs/search"
        parametros = {
            "api_key": GIPHY_API_KEY,
            "q": termo,
            "limit": 5
        }
        resposta = requests.get(url, params=parametros)
        if resposta.status_code == 200:
            dados = resposta.json()
            for item in dados["data"]:
                gifs.append(item["images"]["original"]["url"])
    return render_template("index.html", gifs=gifs)

if __name__ == "__main__":
    app.run(debug=True)
