from flask import Flask
from flask_migrate import Migrate
from routes.routes import image, description
from models.data import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    return app

app = create_app()

app.register_blueprint(image, url_prefix='/image')
app.register_blueprint(description, url_prefix='/desc')
migrate = Migrate(app, db)

if __name__ == '__main__':  # Running the app
    app.run(port=5001, debug=True)