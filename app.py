from flask import Flask, render_template, request, url_for
import sqlite3


app = Flask(__name__)
@app.route('/')
def default():
   return render_template('home.html')


@app.route('/home')
def home():
   return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
   if request.method=='POST':
      userName=request.form['name']
      userPassword=request.form['passWord']
      if userName=='admin' and userPassword=='1234':
         return render_template('dashboard.html', name=userName)
      else:
         return render_template('home.html')
   else:
      userName=request.args.get('name')
      return render_template('login.html', name=userName)



if __name__ == '__main__':
   app.run()