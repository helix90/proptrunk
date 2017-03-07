from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template(index.html)

@app.route('/inventory')
def inventory():
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
def reports():
    return 'Repoert'

if __name__ == '__main__':
    app.run()
