from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    category = db.Column(db.String(50), nullable=False, default='General')
    priority = db.Column(db.String(50), nullable=False, default='Medium')
    due_date = db.Column(db.DateTime, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    categories = Task.query.with_entities(Task.category).distinct()
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks, categories=categories, today=datetime.utcnow().date())

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    description = request.form.get('description')
    category = request.form.get('category')
    priority = request.form.get('priority')
    due_date = request.form.get('due_date')
    if due_date:
        due_date = datetime.strptime(due_date, '%Y-%m-%d')
    
    new_task = Task(title=title, description=description, category=category, priority=priority, due_date=due_date)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    task = Task.query.get(id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    tasks = Task.query.filter(Task.title.contains(query) | Task.description.contains(query)).all()
    categories = Task.query.with_entities(Task.category).distinct()
    return render_template('index.html', tasks=tasks, categories=categories, today=datetime.utcnow().date())

@app.route('/filter/<string:category>')
def filter(category):
    tasks = Task.query.filter_by(category=category).all()
    categories = Task.query.with_entities(Task.category).distinct()
    return render_template('index.html', tasks=tasks, categories=categories, today=datetime.utcnow().date())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
    
from datetime import datetime

@app.route('/')
def index():
    today = datetime.today().strftime('%B %d, %Y')
    categories = db.session.query(Task.category.distinct()).all()
    tasks = Task.query.all()
    return render_template('index.html', today=today, categories=categories, tasks=tasks)
    