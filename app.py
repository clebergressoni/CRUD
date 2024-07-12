from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def get_user():
    user_data = {
        'name':'cleber',
        'age': 12,
        'email': 'cleber@gmail.com'        
    }

    return jsonify(user_data), 200



if __name__ == "__main__":
    app.run(debug=True)
