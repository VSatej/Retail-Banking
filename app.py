from flask import Flask,render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()
