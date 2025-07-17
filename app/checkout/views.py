from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from . import checkout
from .. import db
from ..models import Thing

@checkout.route('/checkout', methods=['GET', 'POST'])
@login_required
def inventory():
    # shopping cart

    items = Thing.query.all()
    # render template
    return render_template('checkout/item.html', items=items, title='Inventory')

@checkout.route('/checkout', methods=['GET', 'POST'])
@login_required
def item():
    # check out a single item
    item = Thing.query()
    return render_template('checkout/item.html', item=item, title='element')