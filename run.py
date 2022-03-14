from distutils.log import debug
from app import create_app, db
from app.auth.models import User

flask_scrapy_app = create_app('dev')
with flask_scrapy_app.app_context():
  db.create_all()
  if not User.query.filter_by(user_name='test').first():
    User.create_user(
      user = 'test',
      email = 'test@test.com',
      password = 'test123'
    )
    
flask_scrapy_app.run(port = 8000)