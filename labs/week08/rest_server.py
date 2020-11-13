from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

books=[{"id": 1, "Title": "Harry Potter", "Author": "JK", "Price": 1000},
{"id": 2, "Title": "some cook book", "Author": "Mr Angry Man", "Price": 2000},
{"id": 3, "Title": "Python made easy", "Author": "Some Liar", "Price": 1500}]

nextId = 4

@app.route('/')
def index():
    return "hello"

@app.route('/books')
def getAll():
    return jsonify(books)

@app.route('/books/<int:id>')
def findById(id):
    foundBooks = list(filter (lambda t: t['id'] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 204
    return jsonify(foundBooks[0])


@app.route('/books', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)
    
    book = {
        "id": nextId,
        "Title": "Test",
        "Author": "Test",
        "Price": 999
    }
    books.append(book)
    nextId +=1
    return jsonify(book)

#curl -i -H "Content-Type:application/json" -X PUT -d '{"Title":"test_title"}' http://localhost:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBooks = list(filter(lambda t: t['id'] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404
    if not request.json:
        abort(400)
    currentBook = foundBooks[0]
    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price']

    return jsonify(currentBook)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    foundBooks = list(filter(lambda t: t['id'] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404
    #if not request.json:
    #    abort(400)
    
    books.remove(foundBooks[0])
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)