from flask import abort, flash, redirect, render_template, url_for, request, jsonify
from flask_login import current_user, login_required

from .. import db
from ..models import Thing
from . import api

@api.route('/api/v1/inventory', methods=['GET'])
@login_required
def get_inventory():
    items = Thing.query.all()
    result = []
    for item in items:
        result.append({
            'id': item.id,
            'barcode': item.barcode,
            'name': item.name,
            'description': item.description,
            'owner_id': item.owner_id,
            'owner': item.company.name if item.company else None
        })
    return jsonify(result), 200

@api.route('/api/v1/inventory', methods=['POST'])
@login_required
def create_inventory_item():
    if not current_user.is_admin:
        return jsonify({'error': 'Admin privileges required'}), 403
    data = request.get_json()
    if not data or not all(k in data for k in ('barcode', 'name', 'description', 'owner_id')):
        return jsonify({'error': 'Missing required fields'}), 400
    item = Thing(
        barcode=data['barcode'],
        name=data['name'],
        description=data['description'],
        owner_id=data['owner_id']
    )
    db.session.add(item)
    db.session.commit()
    return jsonify({'id': item.id}), 201

@api.route('/api/v1/inventory/<int:item_id>', methods=['GET'])
@login_required
def get_inventory_item(item_id):
    item = Thing.query.get_or_404(item_id)
    return jsonify({
        'id': item.id,
        'barcode': item.barcode,
        'name': item.name,
        'description': item.description,
        'owner_id': item.owner_id,
        'owner': item.company.name if item.company else None
    }), 200

@api.route('/api/v1/inventory/<int:item_id>', methods=['PUT', 'PATCH'])
@login_required
def update_inventory_item(item_id):
    if not current_user.is_admin:
        return jsonify({'error': 'Admin privileges required'}), 403
    item = Thing.query.get_or_404(item_id)
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
    for field in ['barcode', 'name', 'description', 'owner_id']:
        if field in data:
            setattr(item, field, data[field])
    db.session.commit()
    return jsonify({'message': 'Item updated'}), 200

@api.route('/api/v1/inventory/<int:item_id>', methods=['DELETE'])
@login_required
def delete_inventory_item(item_id):
    if not current_user.is_admin:
        return jsonify({'error': 'Admin privileges required'}), 403
    item = Thing.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted'}), 200