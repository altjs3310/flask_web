from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from apps.crud.forms import UserForm
from apps.crud.models import User
from apps.app import db

crud = Blueprint(
  "crud", # 블루프린트의 이름 지정
  __name__, # 블루프린트가 정의된 모듈명
  template_folder="templates", # 해당 블루프린트와 관련된 템플릿 파일이 있는 폴더
  static_folder="static" # 해당 블루프린트와 관련된 정적 파일이 있는 폴더
)

@crud.route('/')
def index():
  return render_template("crud/index.html")

@crud.route("/users/new", methods=['GET', 'POST'])
def create_user():
  form = UserForm()

  if form.validate_on_submit():
    # 유효성 검사 통과 후 처리될 코드
    user = User(
      username = form.username.data,
      email = form.email.data,
      password = form.password.data
    )

    # insert
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('crud.users'))

  return render_template('crud/create.html', form=form)

@crud.route('/form/test', methods=['GET', 'POST'])
def form_test():
  if request.method == 'POST':
    print(request.form.get('username'))
    print(request.form['email'])
    print(request.form['password'])

  return render_template('crud/formtest.html')

# 회원 목록 페이지로 이동
@crud.route('/users')
@login_required
def users():
  # 데이터베이스에서 전체 레코드를 꺼내오기
  # users = db.session.query(User).all() # select * from users
  users = User.query.all()

  return render_template('crud/index.html', users=users)

@crud.route('/users/<user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
  form = UserForm()
                             # column명 == 값
  # user = User.query.filter(User.id == user_id)      
  # user = User.query.get(user_id) # JPA에 findById                   
  user = User.query.filter_by(id = user_id).first()

  if form.validate_on_submit():
    user.username = form.username.data
    user.email = form.email.data
    user.password = form.password.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('crud.users'))

  return render_template('crud/edit.html', user=user, form=form)

"""  모델 객체 반환
get(): 기본키 컬럼에 해당하는 레코드를 모델 객체로 리턴(first, one, all)

Query객체: SQL문 => 쿼리문만 있으므로 추가적으로 all, first 작업을 더 해야 레코드 조회가능
(filter_by, filter, order_by(컬럼):정렬, limit(개수):개수까지만 결과, distinct():중복제거)
"""

@crud.route('/users/<user_id>/delete', methods=['POST'])
def delete_user(user_id):
  user = User.query.filter_by(id=user_id).first()

  db.session.delete(user)
  db.session.commit()

  return redirect( url_for('crud.users') )