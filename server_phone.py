from flask import request
from flask import render_template
from flask import Flask
from dotenv import load_dotenv
import random
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
    IDs=['20604960313', '21715093102', '20503125319']
    Transaction_ID=random.choice(IDs)
    recipient=request.args.get('recipient')
    expression1=re.compile(r'(\*182\*1\*1\*)(\d+)\*(\d+)\#?')
    expression2=re.compile(r'(\*182\*8\*1\*)(\d+)\*(\d+)\#?')
    if expression1.findall(display):
        for exp in expression1.findall(display):
            number=int(exp[1])
            amount=int(exp[2])
        return render_template('for_phone.html',number=number,amount=amount, cond=True)
    
    elif expression2.findall(display):
        for exp in expression2.findall(display):
            number=int(exp[1])
            amount=int(exp[2])
        return render_template('for_phone.html', number=number, amount=amount, cond=False, recipient=recipient, Transaction_ID=Transaction_ID)
    
if __name__=="__main__":
    app.run(host='0.0.0.0', port='8000')