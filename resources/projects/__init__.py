from .metadata import register_meta
from flask import jsonify
from .projectJson import register_json
from .projectAssets import register_asset
from .createProject import create_project

def register_projects(app):
    register_meta(app, jsonify)
    register_json(app, jsonify)
    register_asset(app, jsonify)
    create_project(app)
