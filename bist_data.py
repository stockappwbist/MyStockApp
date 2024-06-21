from flask import Flask, request, jsonify
import yfinance as yf
from datetime import datetime
import utils
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/get_currency/<cur_name>/")
def get_currency_price(cur_name):
    search = f"{cur_name}"

    url = f"https://www.google.com/search?q={search}"
    req = requests.get(url)

    sor = BeautifulSoup(req.text, "html.parser")

    result = sor.find("div", class_='BNeawe').text
    float_result = utils.calc_currency_number(result)

    return jsonify({'cur_dollar': float_result})


@app.route("/")
def r_hello_world():
    return "Hello World"


@app.route("/stock_info")
def get_stock_information():
    ticker = request.args.get('stock_name') + "." + "IS"
    date_args = request.args.get('date_par')
    user_price = request.args.get('user_price')
    d_now = datetime.now().date()
    data = yf.download(ticker, end=date_args)
    if not user_price:
        return jsonify({'old_price': round(data['Close'].iloc[-1], 3)})

    data_cur = yf.download(ticker, end=d_now)
    return_js = utils.calc_stock_w_date(float(user_price), data['Close'].iloc[-1], data_cur['Close'].iloc[-1])

    return jsonify(return_js)


if __name__ == '__main__':
    app.run(debug=True)


