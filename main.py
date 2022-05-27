from flask import Flask, render_template, request
from lib.coin_api import CoinDataAPIClient
from replit import db

coin_api_client = CoinDataAPIClient()
app = Flask("app")

if "users" not in db:
  db["users"] = {}


@app.route("/", methods=["GET","POST"])
def index():
  if request.method == "GET":
    users = db["users"]
    return render_template("index.html", users = users)
  else:
    users = db["users"]
    username = request.form.get("username")
    users[username] = []
    return render_template("index_html", users=users)

@app.route("/api/coins/<symbol>", methods=["GET"])
def api(symbol):
  coin_info = coin_api_client.get_coin_info(symbol)
  return coin_info

app.run(host="0.0.0.0", port=8000)