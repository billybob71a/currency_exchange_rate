from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)

api = Api(app)


with open("FX_RATES_ANNUAL-sd-2017-01-01.json", "r") as f:
    exchange_dict_list = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

parser = reqparse.RequestParser()
parser.add_argument('country',type=str)
parser.add_argument('year',type=str)

class ExchangeRate(Resource):
     def get(self):
         #args = parser.parse_args()
         country = request.args.get('currency')
         year = request.args.get('year')
         #the statement below is to see if we get the year
         #print("the country is {} and the year is {}".format(country, year))
         for i in exchange_dict_list['observations']:
             print("keys are {}".format(i.keys()))
             if i['d'] == year:
                 try:
                     print(i[country]['v'])
                     return i[country]['v'], 200
                 except KeyError as e:
                    return "Not found", 404

             #print("hello {}".format(i[country]))

         #return {'Currency': country}

#         item = next(filter(lambda x: x['name'] == name, items), None)
#         return {'item': item}, 200 if item else 404
#
# class ItemList(Resource):
#     def get(self):
#         raise print("Hello")
#         return {'items': items}
#
api.add_resource(ExchangeRate, '/exchangerate') # http://localhost:80/exchangerate?currency=FXAHKDCAD&year=2018-01-01
# api.add_resource(ItemList, '/items')

app.run(host='0.0.0.0', port=80, debug=True)
