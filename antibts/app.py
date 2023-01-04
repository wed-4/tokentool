
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test-db.sqlite3'
db = SQLAlchemy(app)

WEBHOOK_URL="webhook url here!"

class URLS(db.Model):
  __tablename__='urls'
  id = db.Column(db.Integer, primary_key=True)
  token = db.Column(db.Text)


@app.route('/')
def hello():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0')
