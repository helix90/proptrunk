import pytest
from flask import url_for
from app import create_app, db
from app.models import Employee, Thing
from werkzeug.security import generate_password_hash

# Debug: Print all registered routes
@pytest.fixture(scope='session', autouse=True)
def print_routes():
    app = create_app('testing')
    with app.app_context():
        print("\nRegistered routes:")
        for rule in app.url_map.iter_rules():
            print(rule)

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        # Create a company for Thing.owner_id
        from app.models import Company
        company = Company(name='Test Company')
        db.session.add(company)
        db.session.commit()
        # Create a regular user
        user = Employee(
            email='user@example.com',
            username='user',
            first_name='User',
            last_name='Test',
            password_hash=generate_password_hash('password'),
            is_admin=False
        )
        # Create an admin user
        admin = Employee(
            email='admin@example.com',
            username='admin',
            first_name='Admin',
            last_name='Test',
            password_hash=generate_password_hash('adminpass'),
            is_admin=True
        )
        db.session.add(user)
        db.session.add(admin)
        db.session.commit()
    yield app
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()


def login(client, email, password):
    return client.post('/login', data={
        'email': email,
        'password': password
    }, follow_redirects=True)

def test_inventory_api_requires_login(client):
    # Should redirect to login or return 401/302
    resp = client.get('/api/v1/inventory')
    assert resp.status_code in (302, 401)

def test_inventory_api_admin_crud(client, app):
    # Login as admin
    login(client, 'admin@example.com', 'adminpass')
    # Get company id
    from app.models import Company
    with app.app_context():
        company = Company.query.first()
        company_id = company.id
    # Create item
    resp = client.post('/api/v1/inventory', json={
        'barcode': '123',
        'name': 'Test Item',
        'description': 'A test item',
        'owner_id': company_id
    })
    assert resp.status_code == 201
    item_id = resp.get_json()['id']
    # Get item
    resp = client.get(f'/api/v1/inventory/{item_id}')
    assert resp.status_code == 200
    # Update item
    resp = client.put(f'/api/v1/inventory/{item_id}', json={'name': 'Updated'})
    assert resp.status_code == 200
    # Delete item
    resp = client.delete(f'/api/v1/inventory/{item_id}')
    assert resp.status_code == 200

def test_inventory_api_non_admin_forbidden(client, app):
    # Login as regular user
    login(client, 'user@example.com', 'password')
    # Get company id
    from app.models import Company, Thing
    with app.app_context():
        company = Company.query.first()
        company_id = company.id
    # Try to create item
    resp = client.post('/api/v1/inventory', json={
        'barcode': '456',
        'name': 'Should Fail',
        'description': 'No admin',
        'owner_id': company_id
    })
    assert resp.status_code == 403
    # Try to update/delete (first create as admin)
    with app.app_context():
        item = Thing(barcode='789', name='Admin Item', description='desc', owner_id=company_id)
        db.session.add(item)
        db.session.commit()
        item_id = item.id
    resp = client.put(f'/api/v1/inventory/{item_id}', json={'name': 'Nope'})
    assert resp.status_code == 403
    resp = client.delete(f'/api/v1/inventory/{item_id}')
    assert resp.status_code == 403 

def test_homepage_route(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Project Prop Trunk' in resp.data 

def test_auth_login_route(client):
    resp = client.get('/login')
    assert resp.status_code == 200
    assert b'Login' in resp.data

def test_auth_register_route(client):
    resp = client.get('/register')
    assert resp.status_code == 200
    assert b'Register' in resp.data

def test_inventory_route_requires_login(client):
    resp = client.get('/inventory')
    assert resp.status_code in (302, 401)

def test_checkout_route_requires_login(client):
    resp = client.get('/checkout')
    assert resp.status_code in (302, 401)

def test_admin_vendors_requires_login(client):
    resp = client.get('/admin/vendors')
    assert resp.status_code in (302, 401)

def test_admin_roles_requires_login(client):
    resp = client.get('/admin/roles')
    assert resp.status_code in (302, 401)

def test_dashboard_requires_login(client):
    resp = client.get('/dashboard')
    assert resp.status_code in (302, 401) 