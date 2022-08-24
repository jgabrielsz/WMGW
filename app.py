import imp
from flask import Flask
from flask_session import Session
from Auth import auth_bp
from Main import main_bp

# Create the Flask app
app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Register all the blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
    