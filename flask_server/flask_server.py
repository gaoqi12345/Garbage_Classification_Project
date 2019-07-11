
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/register')
def register01():
    return send_file('templates/register.html')

if __name__ == '__main__':
    app.run(debug=True,port=9999)
