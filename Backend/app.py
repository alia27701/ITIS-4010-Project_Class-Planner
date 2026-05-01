# I am creating a Flask app for the Class Planner.
# I want to set up a basic Flask application with a simple route.


app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Class Planner!'

