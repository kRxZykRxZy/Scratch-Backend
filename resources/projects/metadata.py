from src import db

def register_meta(app, jsonify):
    @app.route('/projects/<int:id>')
    def meta(id):
        result = db.query(f"SELECT metadata FROM projects WHERE id = {id}")
        return jsonify(result)
