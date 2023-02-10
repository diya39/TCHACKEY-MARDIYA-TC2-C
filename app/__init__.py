from flask import Flask
from .authentification import login,signup,index,logout,profil
from flask_login import LoginManager,login_required
from .models import db,User

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"]= "it's mine"

    db.init_app(app)
    
    app.route('/login', methods=['GET', 'POST'])(login)
    app.route('/signup', methods=['GET', 'POST'])(signup)
    app.route('/logout')(logout)
    app.route('/', methods=['GET', 'POST'])(index)
    app.route('/profil', methods=['GET', 'POST'])(login_required(profil))
    
    

    return app


