import os
from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/button', methods=['POST'])
def button():
     num = 5
     return redirect(5*num) 
     
@app.route('/number', methods=['POST'])
def number():
    num=request.form('Number')
    return str(5*5)
    
	   
if __name__ == '__main__':
    app.run()
