from metadata import register_meta
from flask import jsonify

def register_projects(app):
  register_meta(app, jsonify)
