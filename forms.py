from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SubmitField, DecimalField
from wtforms.validators import InputRequired, Email, Length, EqualTo, DataRequired, NumberRange

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class ExpenseForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired(), NumberRange(min=0.01)])
    category = SelectField('Category', choices=[('Food', 'Food'), ('Transport', 'Transport'), ('Entertainment', 'Entertainment'), ('Other', 'Other')], validators=[DataRequired()])
    description = StringField('Description')
    submit = SubmitField('Add Expense')