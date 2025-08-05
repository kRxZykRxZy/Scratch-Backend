import base64
import io
import zipfile
import mimetypes
from flask import abort, send_file
from src import db

def register_asset(app, jsonify):
    @app.route('/internalapi/asset/<asset_md5ext>')
    def get_asset(asset_md5ext):
        # Fetch the base64-encoded .sb3 string from the database
        result = db.query("SELECT projectSb3 FROM projects ORDER BY id DESC LIMIT 1;")

        if not result or 'projectSb3' not in result[0]:
            return abort(404, "Project not found")

        try:
            encoded_sb3 = result[0]['projectSb3']
            sb3_bytes = base64.b64decode(encoded_sb3)
            zip_buffer = io.BytesIO(sb3_bytes)

            with zipfile.ZipFile(zip_buffer, 'r') as zip_file:
                # Check if the requested asset is in the zip archive
                if asset_md5ext not in zip_file.namelist():
                    return abort(404, "Asset not found in sb3")

                asset_data = zip_file.read(asset_md5ext)

                # Guess MIME type (e.g., image/png, audio/mpeg, etc.)
                mime_type, _ = mimetypes.guess_type(asset_md5ext)
                if not mime_type:
                    mime_type = 'application/octet-stream'

                return send_file(
                    io.BytesIO(asset_data),
                    mimetype=mime_type,
                    as_attachment=False,
                    download_name=asset_md5ext
                )

        except Exception as e:
            return abort(500, f"Failed to extract asset: {str(e)}")
