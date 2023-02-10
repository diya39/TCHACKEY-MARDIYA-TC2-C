from app import create_app
from flask_sqlalchemy import SQLAlchemy
from app.models import db,User
from flask_login import LoginManager,login_required

app = create_app()
login_manager = LoginManager()
login_manager.login_view = 'authentification.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    
        return User.query.get(int(user_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
