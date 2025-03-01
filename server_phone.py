from flask import request
from flask import render_template
from flask import Flask
from dotenv import load_dotenv
import re
import os

load_dotenv()

app=Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    My_kit=os.getenv('My_kit')
    return render_template('numpad.html',My_kit=My_kit )

@app.route('/phone')
def phone():
    display=request.args.get('display')
    expression=re.compile(r'(\*182\*1\*1\*)(\d+)\*(\d+)\#?')
    for exp in expression.findall(display):
        number=int(exp[1])
        amount=int(exp[2])
    return render_template('for_phone.html',number=number,amount=amount)

if __name__=="__main__":
    app.run(host='0.0.0.0', port='8000')