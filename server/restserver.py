#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response, json
from statesDAO import statesDAO

app = Flask(__name__,
            static_url_path='', 
            static_folder='../static_folder')


@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/states', methods=['GET'])
def get_states():
    states = statesDAO.getAll()
    
    return jsonify(states)
# curl -i http://localhost:5000/states

@app.route('/ecvtotals', methods=['GET'])
def get_ecvtotal():
    ttotal = 0
    btotal = 0
    states = statesDAO.getAll()
    for state in states:
        if state['tv'] > state['bv']:
            ttotal += state['ecv']
        else:
            btotal += state['ecv']
    ecv = {"tecv": ttotal,
            "becv": btotal}

    return jsonify( {'ECV':ecv })


@app.route('/states/<string:abv>', methods =['GET'])
def findStateByAbv(abv):
    foundState = statesDAO.findByAbv(abv)

    return jsonify(foundState)
#curl -i http://localhost:5000/states/TX


@app.route('/states/<string:abv>', methods=['PUT'])
def update_state(abv):
    foundState = statesDAO.findByAbv(abv)
    
    if not foundState:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    
    if 'tv' in request.json and type(request.json['tv']) is not int:
        abort(400)
    if 'bv' in request.json and type(request.json['bv']) is not int:
        abort(400)
 

    foundState['name']  = request.json.get('name', foundState['name'])
    foundState['ecv'] = request.json.get('ecv', foundState['ecv'])
    foundState['tv'] = request.json.get('tv', foundState['tv'])
    foundState['bv'] = request.json.get('bv', foundState['bv'])
    foundState['tp'] = request.json.get('tp', foundState['tp'])
    foundState['bp'] = request.json.get('bp', foundState['bp'])
    values = (foundState['tv'],foundState['bv'],foundState['tp'],foundState['bp'],foundState['abv'])
    statesDAO.update(values)
    return jsonify(foundState)
#curl -i -H "Content-Type:application/json" -X PUT -d '{"name": "AAlaska"}' http://localhost:5000/states/AK




if __name__ == '__main__' :
    app.run(debug= True)