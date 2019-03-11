from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloFrom(FlaskForm):
    name = StringField('name', render_kw={'class': 'input-name', }, validators=[DataRequired(), Length(1, 20)])
    message = TextAreaField('message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()
