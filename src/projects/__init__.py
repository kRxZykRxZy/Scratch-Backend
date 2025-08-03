from metadata import register_meta
from flask import jsonify
from projectJson import register_json

def register_projects(app):
  register_meta(app, jsonify())
  register_json(app, jsonify()) 
