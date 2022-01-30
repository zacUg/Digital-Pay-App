from DigitalPay import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')


#Can also be done using app.py    
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Algorand Balance"
"""
#The reason we’ve structured it like this is for a lot more flexibility. 
# As we start adding more features, a single app.py will quickly become overcrowded and hard to use. 
# What we’ve done is used a Flask Blueprint to separate components.