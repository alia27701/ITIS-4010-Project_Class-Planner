from datetime import date, timedelta

from flask import Flask, jsonify, request


app = Flask(__name__)

# Higher priority = lower number (Exam first, then Project, Quiz, Homework)
_CATEGORY_PRIORITY = {
    'Exam': 0,
    'Project': 1,
    'Quiz': 2,
    'Homework': 3,
}

# Stub users until a database exists (placeholder login only)
_PLACEHOLDER_USERS = {
    'demo': 'password123',
}

_classes: list[dict] = []
_next_class_id = 1

# Each item: id, title, due_date (YYYY-MM-DD), category (Exam|Project|Quiz|Homework)
_assignments: list[dict] = []


# -----------------------------------------------------------------------------
# General (home, health checks, etc.)
# -----------------------------------------------------------------------------


@app.route('/')
def home():
    return 'Welcome to the Class Planner!'


@app.route('/test')
def test():
    return jsonify(message='API working')


# -----------------------------------------------------------------------------
# Auth — login, register, sessions / tokens, password reset, etc.
# -----------------------------------------------------------------------------
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json(silent=True) or {}
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify(error='username and password are required'), 400

    # No persistence yet — stub success response
    return jsonify(message='User registered successfully', username=username), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True) or {}
    username = (data.get('username') or '').strip()
    password = (data.get('password') or '').strip()

    if not username or not password:
        return jsonify(error='username and password are required'), 400

    if len(username) < 3:
        return jsonify(error='username must be at least 3 characters'), 400

    if len(password) < 6:
        return jsonify(error='password must be at least 6 characters'), 400

    expected = _PLACEHOLDER_USERS.get(username)
    if expected is None or expected != password:
        return jsonify(error='invalid username or password'), 401

    return jsonify(message='Login successful', username=username), 200


# -----------------------------------------------------------------------------
# Classes — courses, schedules, sections, enrollment, etc.
# -----------------------------------------------------------------------------


@app.route('/classes', methods=['GET'])
def list_classes():
    return jsonify(classes=_classes)


@app.route('/classes', methods=['POST'])
def add_class():
    global _next_class_id

    data = request.get_json(silent=True) or {}
    name = (data.get('name') or '').strip()
    subject = (data.get('subject') or '').strip()

    if not name or not subject:
        return jsonify(error='name and subject are required'), 400

    new_class = {
        'id': _next_class_id,
        'name': name,
        'subject': subject,
    }
    _classes.append(new_class)
    _next_class_id += 1

    return jsonify(new_class), 201


# -----------------------------------------------------------------------------
# Assignments — tasks, due dates, submissions, etc.
# -----------------------------------------------------------------------------


@app.route('/reminders', methods=['GET'])
def generate_reminders():
    today = date.today()
    last_day = today + timedelta(days=6)  # next 7 calendar days including today

    upcoming = []
    for a in _assignments:
        try:
            due = date.fromisoformat(a['due_date'])
        except (KeyError, TypeError, ValueError):
            continue
        if today <= due <= last_day:
            upcoming.append(a)

    upcoming.sort(
        key=lambda a: (
            _CATEGORY_PRIORITY.get(a.get('category'), 99),
            a.get('due_date', ''),
        )
    )
    return jsonify(reminders=upcoming)


if __name__ == '__main__':
    app.run(debug=True)
