import base64
import json
from flask import request, jsonify, session
from src import db  # your db import

def save_project_sb3(app):
    @app.route('/users/<username>/projects/<int:project_id>/save', methods=['POST'])
    def save_sb3(username, project_id):
        # Check user session auth
        if username != session.get("username"):
            return jsonify({"error": "Unauthorized", "success": False}), 403
        
        # Check if file part is present
        if 'file' not in request.files:
            return jsonify({"error": "No file part in request", "success": False}), 400
        
        file = request.files['file']

        # Check file is sb3
        if file.filename == '' or not file.filename.endswith('.sb3'):
            return jsonify({"error": "No sb3 file uploaded", "success": False}), 400
        
        # Read file content and encode to base64
        file_bytes = file.read()
        encoded_sb3 = base64.b64encode(file_bytes).decode('utf-8')
        
        # Update project in DB
        update_result = db.query("""
            UPDATE projects
            SET projectSb3 = %s
            WHERE id = %s AND author = %s
        """, (encoded_sb3, project_id, username))

        # You might want to check if the update affected any rows
        if update_result is None:  # assuming your db.query returns None if no rows updated
            return jsonify({"error": "Project not found or unauthorized", "success": False}), 404

        return jsonify({"success": True, "message": "Project saved successfully"}), 200
