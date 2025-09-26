from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class WriteForm(FlaskForm):
  subject = StringField(
    "제목",
    validators=[
      DataRequired(message="제목은 필수입니다."),
      Length(max=30, message="제목은 30자 이내로 입력")
    ]
  )

  content = TextAreaField(
    "내용",
    validators=[
      DataRequired(message="내용은 필수입니다."),
    ]
  )

  writer = StringField(
    "작성자",
    validators=[
      DataRequired(message="작성자는 필수입니다."),
      Length(max=10, message="작성자는 10자 이내로 입력")
    ]
  )

  submit = SubmitField("작성하기")