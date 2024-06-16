# Example code for creating a new user
import os
from flask import app, jsonify, request
from werkzeug.utils import secure_filename
from app import User
from manage import app, db

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], password=data['password'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

# Example code for retrieving user details
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({'username': user.username, 'role': user.role})

# Example code for updating user information
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    user.username = data['username']
    user.role = data['role']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

# Example code for deleting a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})


@app.route('/meeting-rooms', methods=['GET'])
def get_optimized_meeting_room():
    # Retrieve meeting room data (e.g., capacities, availability) from the database or another data source
    meeting_rooms = [
        {'name': 'Meeting Room A', 'capacity': 10, 'availability': True},
        {'name': 'Meeting Room B', 'capacity': 8, 'availability': False},
        {'name': 'Meeting Room C', 'capacity': 12, 'availability': True}
        # Add more meeting room data as needed
    ]

    # Extract required capacity from query parameters
    required_capacity = int(request.args.get('capacity', 0))

    # Filter available meeting rooms based on criteria (e.g., capacity, availability)
    available_rooms = [room for room in meeting_rooms if room['availability']]

    # Determine the best meeting room based on capacity and other requirements
    best_room = None
    for room in available_rooms:
        if room['capacity'] >= required_capacity:
            best_room = room
            break  # Found the best room, exit the loop

    if best_room:
        return jsonify({'message': f'Best meeting room suggested: {best_room["name"]}', 'room_info': best_room})
    else:
        return jsonify({'message': 'No suitable meeting room available'})

@app.route('/upload-floor-plan', methods=['POST'])
def upload_floor_plan():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    # If user does not select a file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file to a designated directory
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Optionally, you can store the file path in the database
        # Example: new_floor_plan = FloorPlan(file_path=file_path)
        # db.session.add(new_floor_plan)
        # db.session.commit()

        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 201
