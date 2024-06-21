from flask import Flask, request, jsonify
import yfinance as yf

app = Flask(__name__)


@app.route("/")
def r_hello_world():
    return jsonify({'msg': 'e'})


@app.route("/stock_info")
def get_stock_information():
    ticker = request.args.get('stock_name') + "." + "IS"
    date_args = request.args.get('date_par')
    user_price = request.args.get('user_price')
    data = yf.download(ticker, end=date_args)
    if not user_price:
        return jsonify({'old_price': round(data['Close'].iloc[-1], 3)})
    return jsonify({'msg': 'e'})

    # data_cur = yf.download(ticker, end=d_now)
    # # return_js = utils.calc_stock_w_date(float(user_price), data['Close'].iloc[-1], data_cur['Close'].iloc[-1])
    #
    # return jsonify(return_js)


if __name__ == '__main__':
    app.run()


