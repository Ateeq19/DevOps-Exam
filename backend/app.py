from flask import Flask, request
import flask
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    text = (
        "Hello from Backend! Ateeq Here. \n"
        "I have successfully run my web app (frontend + backend)!. \n"
        "This is a simple Flask backend server. After this I've made a separate Docker Container for both frontend and backend. \n"
        "Finally, I've used Docker-Compose to run both containers together. Cheers!"
    )
    # Replace newlines with <br> for HTML
    return text.replace("\n", "<br>")

@app.route('/users', methods=["GET", "POST"])
def users():
    print("users endpoint reached...")
    if request.method == "GET":
        with open("users.json", "r") as f:
            data = json.load(f)
            data.append({
                "username": "user4",
                "pets": ["hamster"]
            })

            return flask.jsonify(data)
    if request.method == "POST":
        received_data = request.get_json()
        print(f"received data: {received_data}")
        message = received_data['data']
        return_data = {
            "status": "success",
            "message": f"received: {message}"
        }
        return flask.Response(response=json.dumps(return_data), status=201)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7070)
