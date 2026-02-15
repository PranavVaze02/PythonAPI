from flask import Flask, request, jsonify

app = Flask(__name__)

users = []
current_id = 1


def standard_response(status, data):
    return jsonify({
        "status": status,
        "data": data
    })


@app.route("/")
def home():
    return "Flask API is running"


@app.route("/users", methods=["GET"])
def get_users():
    return standard_response("success", users), 200


@app.route("/users", methods=["POST"])
def add_user():
    global current_id

    data = request.get_json()

    if not data or "name" not in data or "email" not in data:
        return standard_response("error", "Missing name or email"), 400

    if "@" not in data["email"]:
        return standard_response("error", "Invalid email format"), 400

    # Prevent duplicate emails
    for user in users:
        if user["email"] == data["email"]:
            return standard_response("error", "Email already exists"), 400

    new_user = {
        "id": current_id,
        "name": data["name"],
        "email": data["email"]
    }

    users.append(new_user)
    current_id += 1

    return standard_response("success", new_user), 201


if __name__ == "__main__":
    app.run(debug=True)
