from flask_wtf import FlaskForm
import wtforms as ws

class UserForm(FlaskForm):
    username = ws.StringField('Имя полбзователя', validators=[
        ws.validators.DataRequired(),
        ws.validators.Length(min=4, max=20)
    ])
    password = ws.PasswordField('Пароль', validators=[
        ws.validators.DataRequired(),
        ws.validators.Length(min=8, max=24)
    ])
    submit = ws.SubmitField('Save')

class EmployeeForm(FlaskForm):
    fullname = ws.StringField('ФИО', validators=[ws.validators.DataRequired(), ])
    phone = ws.StringField('Номер телефона', validators=[ws.validators.DataRequired(), ])
    short_info = ws.TextAreaField('О себе', validators=[ws.validators.DataRequired(), ])
    experience = ws.IntegerField('Опыт работы', validators=[ws.validators.DataRequired(), ])
    preferred_position = ws.StringField('Предпочитаемый позиция')
    submit = ws.SubmitField('Save')
