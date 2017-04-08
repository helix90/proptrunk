from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('templates/index.html'. title='Prop Trunk')

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return 'Inventory'

@app.route('/inventory', methods=['POST'])
def post_inventory():
    # Process post body (JSON)
    # Insert
    # return object id
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
