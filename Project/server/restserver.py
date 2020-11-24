#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

states = [
    {
        "abv":"WV",
        "name":"West Virginia",
        "tv":545051,
        "bv":235847,
        "ecv": 5
    },
       { "abv":"AK",
        "name":"Alaska",
        "tv":189457,
        "bv":153551,
        "ecv": 3
       }
]

@app.route('/states', methods=['GET'])
def get_states():
    return jsonify( {'states':states})
# curl -i http://localhost:5000/states

@app.route('/states/<string:abv>', methods =['GET'])
def get_state(abv):
    foundStates = list(filter(lambda t : t['abv'] == abv , states))
    if len(foundStates) == 0:
        return jsonify( { 'state' : '' }),204
    return jsonify( { 'state' : foundStates[0] })
#curl -i http://localhost:5000/cars/test

#@app.route('/cars', methods=['POST'])
#def create_car():
#    if not request.json:
#        abort(400)
#    if not 'reg' in request.json:
#        abort(400)
#    car={
#        "reg":  request.json['reg'],
#        "make": request.json['make'],
#        "model":request.json['model'],
#        "price":request.json['price']
#    }
#    cars.append(car)
#    return jsonify( {'car':car }),201
# sample test
# curl -i -H "Content-Type:application/json" -X POST -d '{"reg":"12 D 1234","make":"Fiat","model":"Punto","price":3000}' http://localhost:5000/cars
# for windows use this one
# curl -i -H "Content-Type:application/json" -X POST -d "{\"reg\":\"12 D 1234\",\"make\":\"Fiat\",\"model\":\"Punto\",\"price\":3000}" http://localhost:5000/cars

#@app.route('/cars/<string:reg>', methods=['PUT'])
#def update_car(reg):
#    foundCars=list(filter(lambda t : t['reg'] == reg, cars))
#    if len(foundCars) == 0:
#        abort(404)
#    if not request.json:
#        abort(400)
#    if 'make' in request.json and type(request.json['make']) != str:
#        abort(400)
#    if 'model' in request.json and type(request.json['model']) is not str:
#        abort(400)
#    if 'price' in request.json and type(request.json['price']) is not int:
#        abort(400)
#    foundCars[0]['make']  = request.json.get('make', foundCars[0]['make'])
#    foundCars[0]['model'] =request.json.get('model', foundCars[0]['model'])
#    foundCars[0]['price'] =request.json.get('price', foundCars[0]['price'])
#    return jsonify( {'car':foundCars[0]})
#curl -i -H "Content-Type:application/json" -X PUT -d '{"make":"Fiesta"}' http://localhost:5000/cars/181%20G%201234
# for windows use this one
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"make\":\"Fiesta\"}" http://localhost:5000/cars/181%20G%201234

#@app.route('/cars/<string:reg>', methods =['DELETE'])
#def delete_car(reg):
#    foundCars = list(filter (lambda t : t['reg'] == reg, cars))
#    if len(foundCars) == 0:
#        abort(404)
#    cars.remove(foundCars[0])
#    return  jsonify( { 'result':True })

#@app.errorhandler(404)
#def not_found404(error):
#    return make_response( jsonify( {'error':'Not found' }), 404)

#@app.errorhandler(400)
#def not_found400(error):
#    return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug= True)