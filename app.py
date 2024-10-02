from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from password import my_password

app = Flask(__name__, template_folder='templates')
app.jinja_env.auto_reload = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://root:{my_password}@localhost/task_manager_db'
db = SQLAlchemy(app)

# Task Model
class Task(db.Model):
    __tablename__ = 'tasks'
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    assigned_to = db.Column(db.String(255))
    description = db.Column(db.Text)
    priority = db.Column(db.Enum('Low', 'Medium', 'High'), default='Medium', nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date)
    days_counter = db.column_property(db.func.datediff(date.today(), start_date))
    progress = db.Column(db.Integer, default=0, nullable=False)
    @property
    def days_counter(self):
        return (date.today() - self.start_date).days

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    tasks = Task.query.all()
    # tasks = [{"title": "Task 1", "progress": 50}, {"title": "Task 2", "progress": 80}]
    return render_template('dashboard.html', tasks=tasks)

# Create task route
@app.route('/task/create', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        new_task = Task(
            title = request.form['title'],
            assigned_to = request.form['assigned_to'],
            description = request.form['description'],
            priority = request.form['priority'],
            start_date = request.form['start_date'],
            due_date = request.form.get('due_date'),
            progress = request.form['progress']
        )
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('dashboard'))
        except Exception as e:
            print(f"Error creating task: {e}")
            return "Error: Task could not be created"
        
    return render_template('create-task.html')

# Task Details route
@app.route('/task/<int:task_id>')
def task_details(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template('task-details.html', task=task)

# Edit task route
@app.route('/task/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.assigned_to = request.form['assigned_to']
        task.description = request.form['description']
        task.priority = request.form['priority']
        task.start_date = request.form['start_date']
        task.due_date = request.form.get('due_date')
        task.progress = request.form['progress']
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('edit-task.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)

