from .. import db

def register_meta(app, jsonify):
  @app.route('/projects/<int:id>')
  def meta(id):
    json = db.query(f"SELECT {id} FROM projects as project; SELECT project.metadata")
    return jsonify(json)
