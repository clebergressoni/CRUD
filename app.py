from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def get_user(id):
    user_data = {
        'name': 'teste',
        'age': 12,
        'email': 'cleber@gmail.com'   
    }

    return jsonify(user_data), 200

@app.route('/create-user', methods = ['POST'])
def create_user():
    data = request.get_json()

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)
