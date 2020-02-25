from flask import Flask
import json
def create_app():
	app = Flask(__name__)
	
	from .views import main
	app.register_blueprint(main)
	return app
 