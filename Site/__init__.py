from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db= SQLAlchemy()
migrate = Migrate()

def Create_App():
    app= Flask(__name__)

    app.config['SECRET_KEY'] = 'Mbogi Genje'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Note_app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app,db)

    from .views import views
    from .auth import auth
     
    #Registering the blueprints 
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import Notes,Users

    login_manager = LoginManager()
    login_manager.login_view = 'auth.Login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def Load_user(id):
        return Users.query.get(int(id))
    
    return app