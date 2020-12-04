# Created by Adrian Donohoe 20/11/2020
#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response, json,  redirect
from StatesDAO import statesDAO



app = Flask(__name__,static_url_path='', static_folder='../static_folder')



@app.route('/')
def home():
    return app.send_static_file('index.html') # anything hitting / will be sent to index.html
    


@app.route('/states', methods=['GET'])   # route for GET hittng /states
def get_states():
    
    states = statesDAO.getAll()       # runs select * from states; using statesDAO object
    
    return jsonify(states)   # returns all states as JSON
# curl -i http://localhost:5000/states for testing

@app.route('/ecvtotals', methods=['GET']) # route for GET hittng /states
def get_ecvtotal():   # Function to calculate Electoral College Votes for each candidate
    
    ttotal = 0
    btotal = 0
    
    states = statesDAO.getAll() # runs select * from states; using statesDAO object
    for state in states:  # iterate over each state, calculate the winner and add to winners Electoral College Votes
        if state['tv'] > state['bv']:
            ttotal += state['ecv']
        else:
            btotal += state['ecv']
    ecv = {"tecv": ttotal,
            "becv": btotal}
    
    return jsonify( {'ECV':ecv })  # return the ECV Total for each candidate


@app.route('/states/<string:abv>', methods =['GET']) # GET route for each state
def findStateByAbv(abv):  # Method to get an individual state from DB
    
    foundState = statesDAO.findByAbv(abv) # Calls the findByAbv method of the DB Object
    
    return jsonify(foundState)  # return the state info
#curl -i http://localhost:5000/states/TX


@app.route('/states/<string:abv>', methods=['PUT'])  # Route for updating the state in the DB
def update_state(abv):
    
    foundState = statesDAO.findByAbv(abv) # First find the state to be updated
    
    
    if not foundState: # if not found return 404
        abort(404)
    if not request.json:  # if not a json request return 400
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str: # if name is not a string return 400
        abort(400)
    
    if 'tv' in request.json and type(request.json['tv']) is not int: # if tv is not a integer return 400
        abort(400)
    if 'bv' in request.json and type(request.json['bv']) is not int: # if bv is not a integer return 400
        abort(400)
 
# each variable is assigned the new value in the request, or it retains its current, if not supplied
    foundState['name']  = request.json.get('name', foundState['name'])
    foundState['ecv'] = request.json.get('ecv', foundState['ecv'])
    foundState['tv'] = request.json.get('tv', foundState['tv'])
    foundState['bv'] = request.json.get('bv', foundState['bv'])
    foundState['tp'] = request.json.get('tp', foundState['tp'])
    foundState['bp'] = request.json.get('bp', foundState['bp'])
    values = (foundState['tv'],foundState['bv'],foundState['tp'],foundState['bp'],foundState['abv'])
    
    statesDAO.update(values) # Run the DB update with new values
    
    return jsonify(foundState)  # Return the state
#curl -i -H "Content-Type:application/json" -X PUT -d '{"name": "AAlaska"}' http://localhost:5000/states/AK




if __name__ == '__main__' :
    app.run(debug= True)