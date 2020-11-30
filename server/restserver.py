#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response, json

app = Flask(__name__,
            static_url_path='', 
            static_folder='../static_folder')

#states = [
#    {
#        "abv":"WV",
#        "name":"West Virginia",
#        "tv":545051,
#        "bv":235847,
#        "ecv": 5
#    },
#       { "abv":"AK",
#        "name":"Alaska",
#        "tv":189457,
#        "bv":153551,
#        "ecv": 3
#       }
#]

with open('../states.json') as f:
    states = json.load(f)

@app.route('/')
def home():
  return app.send_static_file('index.html')

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
#curl -i http://localhost:5000/states/TX

@app.route('/states', methods=['POST'])
def create_state():
    if not request.json:
        abort(400)
    if not 'abv' in request.json:
        abort(400)
    state={
        "abv":  request.json['abv'],
        "name": request.json['name'],
        "ecv":request.json['ecv'],
        "tv":request.json['tv'],
        "bv":request.json['bv'],
        "tp":request.json['tp'],
        "bp":request.json['bp'],
    }
    states.append(state)
    return jsonify( {'state':state }),201
# sample test Linux
# curl -i -H "Content-Type:application/json" -X POST -d '{"abv":"ZZ","name":"Zedzed","ecv":4,"tv":3000,"bv": 10000,"tp": 10,"bp": 80}' http://localhost:5000/states

@app.route('/states/<string:abv>', methods=['PUT'])
def update_state(abv):
    foundStates=list(filter(lambda t : t['abv'] == abv, states))
    if len(foundStates) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    
    if 'tv' in request.json and type(request.json['tv']) is not int:
        abort(400)
    if 'bv' in request.json and type(request.json['bv']) is not int:
        abort(400)
    #if 'tp' in request.json and type(float(request.json['tp'])) is not float:
    #    abort(400)
    #if 'bp' in request.json and type(float(request.json['bp'])) is not float:
    #    abort(400)

    foundStates[0]['name']  = request.json.get('name', foundStates[0]['name'])
    foundStates[0]['ecv'] = request.json.get('ecv', foundStates[0]['ecv'])
    foundStates[0]['tv'] = request.json.get('tv', foundStates[0]['tv'])
    foundStates[0]['bv'] = request.json.get('bv', foundStates[0]['bv'])
    foundStates[0]['tp'] = request.json.get('tp', foundStates[0]['tp'])
    foundStates[0]['bp'] = request.json.get('bp', foundStates[0]['bp'])
    return jsonify( {'state':foundStates[0]})
#curl -i -H "Content-Type:application/json" -X PUT -d '{"name": "AAlaska"}' http://localhost:5000/states/AK

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