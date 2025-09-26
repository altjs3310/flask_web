from apps.app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime

class User(db.Model, UserMixin):
  # db에 생성되는 테이블명 지정
  __tablename__ = "users"

  # 컬럼들...
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), index=True)
  email = db.Column(db.String(255), unique=True, index=True)
  password_hash = db.Column(db.String(255))
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

  @property
  def password(self):
    raise AttributeError("읽을 수 없음")
  
  @password.setter
  def password(self, password):
    self.password_hash = generate_password_hash(password)

  # 비밀번호 체크
  def verify_password(self, password):
    return check_password_hash(self.password_hash, password)

  # 메일 중복 검사
  def is_duplicate_email(self):
    # select * from users where email=self.email
    return User.query.filter_by(email=self.email).first() is not None
  
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)  

"""
  db.integer:정수
  db.String:문자열(varchar)
  db.Text:긴문자열
  db.Float:실수
  db.Boolean:불린
  db.Date:날짜
  db.Time:시간
  db.DateTime:날짜와 시간

  옵션(제약조건)
  primary_key=True:기본키
  unique=True:중복불가능
  nullable=False:널값 불가능
  default=xxx:기본값
  index=True:인덱스 생성
"""