from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import VendorForm, EmployeeAssignForm, RoleForm
from .. import db
from ..models import Vendor, Employee, Role


def check_admin():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)


# Vendor Views


@admin.route('/vendors', methods=['GET', 'POST'])
@login_required
def list_vendors():
    """
    List all vendors
    """
    check_admin()

    vendors = Vendor.query.all()

    return render_template('admin/vendors/vendors.html',
                           vendors=vendors, title="Vendors")


@admin.route('/vendors/add', methods=['GET', 'POST'])
@login_required
def add_vendor():
    """
    Add a vendor to the database
    """
    check_admin()

    add_vendor = True

    form = VendorForm()
    if form.validate_on_submit():
        vendor = Vendor(name=form.name.data,
                                description=form.description.data)
        try:
            # add vendor to the database
            db.session.add(vendor)
            db.session.commit()
            flash('You have successfully added a new vendor.')
        except:
            # in case vendor name already exists
            flash('Error: vendor name already exists.')

        # redirect to vendors page
        return redirect(url_for('admin.list_vendors'))

    # load vendor template
    return render_template('admin/vendors/vendor.html', action="Add",
                           add_vendor=add_vendor, form=form,
                           title="Add Vendor")


@admin.route('/vendors/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_vendor(id):
    """
    Edit a vendor
    """
    check_admin()

    add_vendor = False

    vendor = Vendor.query.get_or_404(id)
    form = VendorForm(obj=vendor)
    if form.validate_on_submit():
        vendor.name = form.name.data
        vendor.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the vendor.')

        # redirect to the vendors page
        return redirect(url_for('admin.list_vendors'))

    form.description.data = vendor.description
    form.name.data = vendor.name
    return render_template('admin/vendors/vendor.html', action="Edit",
                           add_vendor=add_vendor, form=form,
                           vendor=vendor, title="Edit Vendor")


@admin.route('/vendors/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_vendor(id):
    """
    Delete a vendor from the database
    """
    check_admin()

    vendor = Vendor.query.get_or_404(id)
    db.session.delete(vendor)
    db.session.commit()
    flash('You have successfully deleted the vendor.')

    # redirect to the vendors page
    return redirect(url_for('admin.list_vendors'))

    return render_template(title="Delete Vendor")


# Role Views


@admin.route('/roles')
@login_required
def list_roles():
    check_admin()
    """
    List all roles
    """
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database
    """
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)

        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    # load role template
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title='Add Role')


@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role
    """
    check_admin()

    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    form.description.data = role.description
    form.name.data = role.name
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database
    """
    check_admin()

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')

    # redirect to the roles page
    return redirect(url_for('admin.list_roles'))

    return render_template(title="Delete Role")


# Employee Views

@admin.route('/employees')
@login_required
def list_employees():
    """
    List all employees
    """
    check_admin()

    employees = Employee.query.all()
    return render_template('admin/employees/employees.html',
                           employees=employees, title='Employees')


@admin.route('/employees/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id):
    """
    Assign a vendor and a role to an employee
    """
    check_admin()

    employee = Employee.query.get_or_404(id)

    # prevent admin from being assigned a vendor or role
    if employee.is_admin:
        abort(403)

    form = EmployeeAssignForm(obj=employee)
    if form.validate_on_submit():
        employee.vendor = form.vendor.data
        employee.role = form.role.data
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully assigned a vendor and role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_employees'))

    return render_template('admin/employees/employee.html',
                           employee=employee, form=form,
                           title='Assign Employee')
