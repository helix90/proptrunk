from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/inventory')
def inventort():
    return 'Inventory'

@app.route('/checkout')
def checkout():
    return 'Checkout'

@app.route('/checkin')
def checkin():
    return 'Checkin'

@app.route('/users')
def user():
    return 'Users'

@app.route('/reports')
def reports()
    return 'Repoert'

if __name__ == '__main__':
    app.run()

