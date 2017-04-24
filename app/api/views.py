from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .. import db
from ..models import Thing

@inventory.route('/api/v1/inventory', methods=['GET', 'POST'])
@login_required
def inventory():
    # show current inventory list

    items = Thing.query.all()
    # Change this to JSON output
    return render_template('inventory/inventory.html', items=items, title='Inventory')