from datetime import date, timedelta
from flask import Flask, jsonify, request

app = Flask(__name__)

# ---------------------------------------------------------------------
# PRIORITY SYSTEM
# ---------------------------------------------------------------------
CATEGORY_PRIORITY = {
    "Exam": 0,
    "Project": 1,
    "Quiz": 2,
    "Homework": 3,
}

# ---------------------------------------------------------------------
# AUTH DATA (TEMPORARY - WILL MOVE TO MYSQL LATER)
# ---------------------------------------------------------------------
USERS = {
    "demo": "password123"
}

# ---------------------------------------------------------------------
# USER DATA STORE (IN-MEMORY SDLC PHASE 1)
# ---------------------------------------------------------------------
data = {
    "demo": {
        "classes": [],
        "assignments": []
    }
}

# ---------------------------------------------------------------------
# HOME / TEST
# ---------------------------------------------------------------------
@app.route("/")
def home():
    return "Class Planner API Running"


@app.route("/test")
def test():
    return jsonify(message="API working")

# ---------------------------------------------------------------------
# AUTH ROUTES
# ---------------------------------------------------------------------
@app.route("/register", methods=["POST"])
def register():
    body = request.get_json() or {}

    username = body.get("username")
    password = body.get("password")

    if not username or not password:
        return jsonify(error="username and password required"), 400

    if username in USERS:
        return jsonify(error="user already exists"), 409

    USERS[username] = password
    data[username] = {"classes": [], "assignments": []}

    return jsonify(message="User registered successfully"), 201


@app.route("/login", methods=["POST"])
def login():
    body = request.get_json() or {}

    username = body.get("username")
    password = body.get("password")

    if USERS.get(username) != password:
        return jsonify(error="invalid credentials"), 401

    return jsonify(message="login successful", user=username), 200

# ---------------------------------------------------------------------
# CLASSES
# ---------------------------------------------------------------------
@app.route("/classes/<user>", methods=["GET"])
def get_classes(user):
    return jsonify(classes=data[user]["classes"])


@app.route("/classes/<user>", methods=["POST"])
def add_class(user):
    body = request.get_json() or {}

    name = body.get("name")
    subject = body.get("subject")

    if not name or not subject:
        return jsonify(error="name and subject required"), 400

    new_class = {
        "id": len(data[user]["classes"]) + 1,
        "name": name,
        "subject": subject
    }

    data[user]["classes"].append(new_class)

    return jsonify(new_class), 201

# ---------------------------------------------------------------------
# ASSIGNMENTS
# ---------------------------------------------------------------------
@app.route("/assignments/<user>", methods=["GET"])
def get_assignments(user):
    return jsonify(assignments=data[user]["assignments"])


@app.route("/assignments/<user>", methods=["POST"])
def add_assignment(user):
    body = request.get_json() or {}

    assignment = {
        "id": len(data[user]["assignments"]) + 1,
        "class_id": body.get("class_id"),
        "title": body.get("title"),
        "due_date": body.get("due_date"),  # YYYY-MM-DD
        "category": body.get("category"),
        "priority": body.get("priority", 3),
        "completed": False
    }

    data[user]["assignments"].append(assignment)

    return jsonify(assignment), 201


@app.route("/assignments/<user>/<int:aid>", methods=["PUT"])
def mark_completed(user, aid):
    for a in data[user]["assignments"]:
        if a["id"] == aid:
            a["completed"] = True
            return jsonify(a)

    return jsonify(error="assignment not found"), 404

# ---------------------------------------------------------------------
# REMINDERS
# ---------------------------------------------------------------------
@app.route("/reminders/<user>", methods=["GET"])
def generate_reminders(user):
    today = date.today()
    end = today + timedelta(days=7)

    upcoming = []

    for a in data[user]["assignments"]:
        if a.get("completed"):
            continue

        try:
            due = date.fromisoformat(a["due_date"])
        except:
            continue

        if today <= due <= end:
            upcoming.append(a)

    upcoming.sort(
        key=lambda x: (
            CATEGORY_PRIORITY.get(x.get("category"), 99),
            x.get("due_date", "")
        )
    )

    return jsonify(reminders=upcoming)

# ---------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)