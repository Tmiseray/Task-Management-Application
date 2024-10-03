from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from jinja2 import FileSystemLoader
from flask_marshmallow import Marshmallow
from flask_bcrypt import bcrypt
# from enum import Enum
from marshmallow import fields
from datetime import date, timedelta
from password import my_password, my_secret_key

# loader = FileSystemLoader('templates')
app = Flask(__name__, template_folder = 'templates')
app.jinja_env.auto_reload = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root:{my_password}@localhost/task_manager_db'
app.secret_key = my_secret_key
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Task Model & Schema
class Task(db.Model):
    __tablename__ = 'Tasks'
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    assigned_to = db.Column(db.String(255))
    description = db.Column(db.Text)
    priority = db.Column(db.Enum('Low', 'Medium', 'High'), default='Medium', nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date)
    days_counter = db.column_property(db.func.datediff(date.today(), start_date))
    progress = db.Column(db.Integer, default=0, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), primary_key=True)
    @property
    def days_counter(self):
        return (date.today() - self.start_date).days
    
    user_task = db.relationship('User', back_populates='task')

class TaskSchema(ma.Schema):
    title = fields.String(required=True)
    assigned_to = fields.String(required=False)
    description = fields.String(required=True)
    priority = fields.String()
    start_date = fields.Date(required=True)
    due_date = fields.Date(required=False)
    progress = fields.Integer(required=True)
    user_id = fields.Integer(required=True)

    class Meta:
        fields = ('task_id', 'title', 'assigned_to', 'description', 'priority', 'start_date', 'due_date', 'progress', 'user_id')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


# User Model & Schema
class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(300), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    contact_phone = db.Column(db.Boolean)
    contact_email = db.Column(db.Boolean)

    account = db.relationship('UserAccount', back_populates='linked_user', uselist=False)
    task = db.relationship('Task', back_populates='user_task', uselist=False)

class UserSchema(ma.Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)
    contact_phone = fields.Boolean(required=False)
    contact_email = fields.Boolean(required=False)

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'contact_phone', 'contact_email')

user_schema = UserSchema()


# CustomerAccount Model & Schema
class UserAccount(db.Model):
    __tablename__ = 'UserAccounts'
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), primary_key=True)
    username = db.Column(db.String(75), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)

    linked_user = db.relationship('User', back_populates='account')

class AccountSchema(ma.Schema):
    user_id = fields.Integer(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)

    class Meta:
        fields = ('user_id', 'username', 'password')

account_schema = AccountSchema()


# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user_id = session['user_id']
        tasks = Task.query.filter_by(user_id = user_id).filter(Task.progress<100).all()
        completed_tasks = Task.query.filter_by(user_id=user_id).filter(Task.progress == 100).all()
        return render_template('dashboard.html', tasks=tasks, completed_tasks=completed_tasks)
    else:
        return redirect(url_for('login'))

# Create task route
@app.route('/task/create', methods=['GET', 'POST'])
def create_task():
    if session:
        if request.method == 'POST':
            due_date = request.form.get('due_date')
            if not due_date:
                due_date = None

            new_task = Task(
                title = request.form.get('title'),
                assigned_to = request.form.get('assigned_to'),
                description = request.form.get('description'),
                priority = request.form.get('priority'),
                start_date = request.form.get('start_date'),
                due_date = due_date,
                progress = request.form.get('progress'),
                user_id = session['user_id']
            )
            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect(url_for('dashboard'))
            except Exception as e:
                print(f"Error creating task: {e}")
                return "Error: Task could not be created"
            
        return render_template('create_task.html')
    else:
        return redirect(url_for('login'))

# Task Details route
@app.route('/task/<int:task_id>')
def task_details(task_id):
    user_id = session.get('user_id')
    task = Task.query.filter_by(task_id=task_id, user_id=user_id).first()
    if task:
        return render_template('task_details.html', task=task)
    return "Task not found", 404

# Edit task route
@app.route('/task/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    user_id = session.get('user_id')
    task = Task.query.filter_by(task_id=task_id, user_id=user_id).first()
    if not task:
        return "Task not found", 404
    
    if request.method == 'POST':
        due_date = request.form.get('due_date')
        if not due_date:
            due_date = None

        task.title = request.form.get('title')
        task.assigned_to = request.form.get('assigned_to')
        task.description = request.form.get('description')
        task.priority = request.form.get('priority')
        task.start_date = request.form.get('start_date')
        task.due_date = due_date
        task.progress = request.form.get('progress')
        db.session.commit()
        return redirect(url_for('dashboard'))
    
    return render_template('edit_task.html', task=task)

# Register User & Account route
@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'GET':
        return render_template('registration.html')
    
    contact_email = request.form.get('contact_email') == 'on'
    contact_phone = request.form.get('contact_phone') == 'on'
    new_user = User(
        first_name = request.form.get('first_name'),
        last_name = request.form.get('last_name'),
        email = request.form.get('email'),
        phone = request.form.get('phone'),
        contact_phone = contact_phone,
        contact_email = contact_email
    )
    try:
        db.session.add(new_user)
        db.session.flush()
    except Exception as e:
        print(f"Error creating new user: {e}")
        return "Error: User could not be created"
    
    user_input = request.form.get('password_input')
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(user_input.encode('utf-8'), salt)
    user_account = UserAccount(
        user_id = new_user.id,
        username = request.form.get('username_input'),
        password = hashed_pw
    )
    try:
        db.session.add(user_account)
        db.session.commit()
        return redirect(url_for('login'))
    except Exception as e:
        db.session.rollback()
        print(f"Error creating user account: {e}")
        return "Error: User account could not be created"

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username_login = request.form.get('username_login')
    password_login = request.form.get('password_login')
    account = UserAccount.query.filter_by(username=username_login).first()
    if account:
        is_valid = bcrypt.checkpw(password_login.encode('utf-8'), account.password.encode('utf-8'))
        if is_valid:
            user = User.query.filter_by(id = account.user_id).first()
            if user:
                session['first_name'] = user.first_name
                session['last_name'] = user.last_name
                session['user_id'] = user.id
                session['logged_in'] = True
                return redirect(url_for('dashboard'))
        return render_template('login.html', message='Invalid username or password')
    return redirect(url_for('register_user'))
          
# Logout Route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('first_name', None)
    session.pop('last_name', None)
    return redirect(url_for('login'))





if __name__ == '__main__':
    app.run(debug=True)

