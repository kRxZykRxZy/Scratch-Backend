from flask import Flask, jsonify
from projects import register_projects  # Ensure 'projects' is a valid module and path

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Scratch Compiler Running",
        "Usage": "https://github.com/kRxZykRxZy/Scratch-Backend"
    })

# Register additional projects (assuming this adds routes to the app)
register_projects(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # Enabling debug for development
