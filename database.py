def init_db(app):
    with app.app_context():
        from models import db
        db.create_all()
