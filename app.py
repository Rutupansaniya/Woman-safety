from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

emergency_contacts = []
location_data = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add-contact', methods=['POST'])
def add_contact():
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')

    if not name or not phone:
        return jsonify({'message': 'Name and phone are required'}), 400

    emergency_contacts.append({
        'name': name,
        'phone': phone
    })
    print(f"[+] Contact added: {name} - {phone}")
    return jsonify({'message': 'Contact added successfully'}), 200

@app.route('/location', methods=['POST'])
def update_location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if latitude is None or longitude is None:
        return jsonify({'message': 'Latitude and longitude are required'}), 400

    location_data['latitude'] = latitude
    location_data['longitude'] = longitude

    print(f"[+] Location received: Latitude = {latitude}, Longitude = {longitude}")
    return jsonify({'message': 'Location updated successfully'}), 200

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(emergency_contacts), 200

@app.route('/location', methods=['GET'])
def get_location():
    return jsonify(location_data), 200

if __name__ == '__main__':
    app.run(debug=True)
