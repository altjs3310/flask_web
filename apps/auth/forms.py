from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignUpForm(FlaskForm):
  username = StringField(
    "사용자명",
    validators=[
      DataRequired(message="사용자명은 필수입니다."),
      Length(min=3, max=20, message="3~20자 이내로 입력")
    ]
  )

  email = StringField(
    "이메일",
    validators=[
      DataRequired(message="이메일은 필수입니다."),
      Email(message="이메일 형식으로 입력")
    ]
  )

  password = PasswordField(
    "비밀번호",
    validators=[
      DataRequired(message="비밀번호는 필수입니다.")
    ]
  )

  submit = SubmitField("가입")


class LoginForm(FlaskForm):
  username = StringField(
    "사용자명",
    validators=[
      DataRequired(message="사용자명은 필수입니다."),
      Length(min=3, max=20, message="3~20자 이내로 입력")
    ]
  )

  password = PasswordField(
    "비밀번호",
    validators=[
      DataRequired(message="비밀번호는 필수입니다.")
    ]
  )

  submit = SubmitField('로그인')