import re

def calc_stock_w_date(user_price, old_stock_price, cur_stock_price):
    stock_number = user_price / old_stock_price
    gain_loss = stock_number * cur_stock_price

    percent_gain_loss = round((gain_loss - user_price) / user_price * 100, 3)

    return_old_price = round(old_stock_price,3)
    return_new_price = round(cur_stock_price,3)
    return_gain_loss = round(gain_loss,3)

    return {'gain_loss': f"%{percent_gain_loss}", 'user_cur_price': return_gain_loss, 'old_price': return_old_price, 'new_price': return_new_price}


def calc_currency_number(currency_text):
    replaced_text = currency_text.replace(",", ".")
    number = re.findall("\d+\.\d+", replaced_text)
    number_float = number and number[0] or 0
    return float(number_float)



