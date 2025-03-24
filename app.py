from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import email_validator

from config import Config
from models import db, User, Expense
from forms import RegisterForm, LoginForm, ExpenseForm


app = Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods =['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created! Please login.", "success")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods =['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password", "danger")
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    user_expenses = Expense.query.filter_by(user_id=current_user.id).all()
    return render_template('expenses.html', expenses=user_expenses)


@app.route('/expenses')
@login_required
def expenses():
    user_expenses = Expense.query.filter_by(user_id=current_user.id).all()
    return render_template('expenses.html', expenses=user_expenses)

@app.route('/add_expense', methods=['POST','GET'])
@login_required
def add_expense():
    form = ExpenseForm()
    if form.validate_on_submit():
        new_expense = Expense(
            amount = form.amount.data,
            category = form.category.data,
            description = form.description.data,
            user_id = current_user.id
        )
        db.session.add(new_expense)
        db.session.commit()
        flash('Expense added Successfully', 'Success')
        return redirect(url_for('expenses'))
    return render_template('add_expense.html', form=form)

@app.route('/delete_expense/<int:expense_id>', methods=['GET','DELETE'])
@login_required
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    
    if expense.user_id != current_user.id:
        flash("Unauthorized action", "danger")
        return redirect(url_for('expenses'))

    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted successfully', 'success')

    return redirect(url_for('expenses'))



if __name__ == '__main__':
    app.run(debug=True)
