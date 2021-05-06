import os
from flask import Flask
from controllers import TodoController, UserController
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = '133da5ef683757d14d5839882ec18807'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

@app.route('/')
def index():
    return TodoController.index()

@app.route('/login')
def login():
    return UserController.login()

@app.route('/signin', methods=['POST'])
def signin():
    return UserController.signin()
    
@app.route('/register')
def register():
    return UserController.register()
 
@app.route('/signup', methods=['POST'])
def signup():
    return UserController.signup()

@app.route('/logout')
def logout():
    return UserController.logout()

@app.route('/create', methods=['POST'])
def create():
    return TodoController.create()

@app.route('/delete/<int:id>')
def delete(id):
    return TodoController.delete(id)

@app.route('/complete/<int:id>')
def complete(id):
    return TodoController.complete(id)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    return TodoController.update(id)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)