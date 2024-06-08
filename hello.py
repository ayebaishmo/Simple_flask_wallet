from flask import Flask, render_template
from wallet import firstuser

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> hello_world </p>"

@app.route("/show_wallet")
def wallet_info1():
    message = firstuser()
    return render_template('wallet.html', message = message)
