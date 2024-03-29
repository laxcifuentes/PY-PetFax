from flask import Flask

def create_app():
    # configure app
    app = Flask(__name__)

    # index routes
    @app.route('/')
    def index():
        return 'Hello, this is PetFax!'
    
    # register pet bp
    from . import pet
    app.register_blueprint(pet.bp)
    
    return app
