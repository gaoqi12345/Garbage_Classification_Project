
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/register')
def register01():
    return send_file('templates/register.html')

@app.route('/forget_password')
def forget_password():
    return send_file('templates/forget_password.html')

@app.route('/reset_password')
def rest_password():
    return send_file('templates/reset_password.html')


if __name__ == '__main__':
    app.run(debug=True)
