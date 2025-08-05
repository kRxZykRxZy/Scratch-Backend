from flask import Flask, jsonify
from .projects import register_projects  # Ensure 'projects' is a valid module and path

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Scratch Compiler Running",
        "Usage": "https://github.com/kRxZykRxZy/Scratch-Backend"
    })

# Register additional projects (assuming this adds routes to the app)
register_projects(app)
