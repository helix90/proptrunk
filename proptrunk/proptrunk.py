from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('templates/index.html', title='Prop Trunk')

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

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run()
