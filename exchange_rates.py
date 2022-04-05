import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
filename = 'rates.text'
table = data[0]
rates = table['rates']


with open('rates.text', 'w') as csvfile:
    fields = ['currency', 'code', 'bid', 'ask']
    csvwriter = csv.DictWriter(csvfile, fieldnames=fields, delimiter=';')

    csvwriter.writeheader()

    for i in rates:
        csvwriter.writerow(i)

for i in rates:
    code_list = (i["code"],i["bid"])
    print(code_list)


