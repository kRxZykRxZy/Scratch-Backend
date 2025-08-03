from metadata import register_meta
from flask import jsonify
from projectJson import register_json
from projectAssets import register_asset

def register_projects(app):
  register_meta(app, jsonify())
  register_json(app, jsonify())
  register_asset(app, jsonify()) 
