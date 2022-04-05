from flask import Flask
from flask import request, redirect
from flask import render_template
import requests
import csv


app = Flask(__name__)

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
filename = 'rates.text'
table = data[0]
rates = table['rates']
codes = [dic['code'] for dic in rates]


@app.route("/waluty", methods=["GET", "POST"])
def strona():
    if request.method == "GET":
        return render_template("currency.html", codes=codes, selected_code=codes[0])
    if request.method == "POST":
        data = request.form
        code = data.get('code')
        quantity = data.get('quantity')
        quantity = float(quantity)
        rate = next((x['bid'] for x in rates if x['code']==code), None)
        if rate is None:
            return 'No rate'
        return render_template("currency.html", codes=codes, selected_code=code, result=str(quantity*rate))





