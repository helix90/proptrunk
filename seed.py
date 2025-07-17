from app import create_app, db
from app.models import Employee, Role

# Use the development config
app = create_app('development')

with app.app_context():
    db.create_all()

    # Ensure 'admin' role exists
    admin_role = Role.query.filter_by(name='admin').first()
    if not admin_role:
        admin_role = Role(name='admin', description='Administrator')
        db.session.add(admin_role)
        db.session.commit()

    # Ensure admin user exists
    admin_email = 'admin@example.com'
    admin_username = 'admin'
    admin_password = 'admin123'  # Change after first login in production!
    admin = Employee.query.filter_by(email=admin_email).first()
    if not admin:
        admin = Employee(
            email=admin_email,
            username=admin_username,
            first_name='Admin',
            last_name='User',
            is_admin=True,
            role=admin_role
        )
        admin.password = admin_password
        db.session.add(admin)
        db.session.commit()
        print(f"Created admin user: {admin_email} / {admin_password}")
    else:
        print(f"Admin user already exists: {admin_email}") 