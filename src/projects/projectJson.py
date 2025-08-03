import base64
import io
import zipfile
import json
from flask import abort
from .. import db

def register_json(app, jsonify):
    @app.route('/projects/<int:id>/contents')
    def json_route(id):
        # Fetch the base64-encoded .sb3 string from the database
        result = db.query(f"SELECT projectSb3 FROM projects WHERE id = {id};")

        if not result or 'projectSb3' not in result[0]:
            return abort(404, "Project not found")

        try:
            encoded_sb3 = result[0]['projectSb3']
            sb3_bytes = base64.b64decode(encoded_sb3)
            zip_buffer = io.BytesIO(sb3_bytes)

            with zipfile.ZipFile(zip_buffer, 'r') as zip_file:
                with zip_file.open('project.json') as json_file:
                    project_data = json.load(json_file)
                    return jsonify(project_data)

        except Exception as e:
            return abort(500, f"Failed to extract project.json: {str(e)}")
