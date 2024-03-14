from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'  # Fixed the database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Todo(db.Model):
    sn = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sn} - {self.title}"

@app.route('/',methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        title= request.form['title']
        desc=request.form['desc']


        todo= Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        allTodo= Todo.query.all()
        return render_template('index.html',allTodo=allTodo)

@app.route('/update')
def update():
    allTodo= Todo.query.all()
    print(allTodo)
    return "This is product page."

@app.route('/delete')
def delete():
    allTodo= Todo.query.all()
    print(allTodo)
    return "This is product page."

if __name__ == "__main__":
    app.run(debug=True)
