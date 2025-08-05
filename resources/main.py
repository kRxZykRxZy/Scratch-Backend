import os
import runpy
from flask import Flask, jsonify
from .projects import register_projects  # your relative import for projects module

# Run the full deps.py script from config folder (project root/config/deps.py)
deps_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config', 'deps.py'))
runpy.run_path(deps_path)

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Scratch Compiler Running",
        "Usage": "https://github.com/kRxZykRxZy/Scratch-Backend"
    })

register_projects(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
