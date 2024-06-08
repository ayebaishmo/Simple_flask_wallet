from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class AccountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    initial_deposit = DecimalField('innitial Deposit', validators=[DataRequired(), NumberRange(min=0)])
    balance  = DecimalField('Balance', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Submit')