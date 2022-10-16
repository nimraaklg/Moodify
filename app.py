from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import time
from moodify.dashboard.templates import main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo:
    main.main()
    time.sleep(10)


    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

