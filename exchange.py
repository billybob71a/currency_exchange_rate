from flask import Flask, request, render_template
from flask_restful import Resource, Api
import json

app = Flask(__name__)

api = Api(app)


with open("FX_RATES_ANNUAL-sd-2017-01-01.json", "r") as f:
    exchange_dict_list = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

class ExchangeRate(Resource):
     def get(self, country):
         print(exchange_dict_list['observations'][country])

         #return {'Currency': country}

#         item = next(filter(lambda x: x['name'] == name, items), None)
#         return {'item': item}, 200 if item else 404
#
# class ItemList(Resource):
#     def get(self):
#         raise print("Hello")
#         return {'items': items}
#
api.add_resource(ExchangeRate, '/exchangerate/<string:country>') # htttp://127.0.0.1:5000/country/HKD
# api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
