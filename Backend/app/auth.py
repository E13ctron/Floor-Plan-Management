from flask import jsonify
from flask_login import login_required, current_user
from manage import app, db
# Example code for protecting routes with authentication
@app.route('/protected', methods=['GET'])
@login_required
def protected_route():
    # Only authenticated users can access this route
    return jsonify({'message': 'This is a protected route'})

# Example code for role-based authorization
def is_admin():
    return current_user.role == 'admin'

@app.route('/admin', methods=['GET'])
@login_required
def admin_route():
    if not is_admin():
        return jsonify({'message': 'Unauthorized'}), 403
    # Only users with admin role can access this route
    return jsonify({'message': 'Welcome admin'})
