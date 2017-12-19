from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import inventory
from .. import db
from ..models import Thing, Image


@app.before_request
def before_request():
    g.user = current_user


@inventory.route('/inventory', methods=['GET', 'POST'])
@login_required
def inventory_list():
    # show current inventory list
    # for the current user (vendor or customer)
    image_list = []
    items = Thing.query.all()
    for item in items:
        tmp_list = Image.query(item=itemid)
        image_list.extend(tmp_list)
    # render template
    # how do we get the image list?
    return render_template('inventory/items.html', items=items, image_list=image_list, title='Inventory')


@inventory.route('/inventory', methods=['GET', 'POST'])
@login_required
def item(itemid=None):
    # show a single item
    # select by item number
    # how do we get the image list?
    item = Thing.query(id=itemid)
    image_list = Image.query(item=itemid)
    return render_template('inventory/item.html', item=item, image_list=image_list, title='element')
