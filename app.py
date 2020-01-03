#!bin/python
from flask import Flask
import primeUtil

app = Flask(__name__)

@app.route('/api/number/is-prime/<num>')
def index(num):
    try:
        int(num)
    except:
        return "Invalid number - " + num
    if (primeUtil.isTwoSidedPrime(num)):
        return "true"
    else: 
        return "false"

if __name__ == '__main__':
    app.run(port=9911, debug=True)
