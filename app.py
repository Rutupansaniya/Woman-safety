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
    data = request.json
    emergency_contacts.append({
        'name': data.get('name'),
        'phone': data.get('phone')
    })
    return jsonify({'message': 'Contact added successfully'}), 200

@app.route('/location', methods=['POST'])
def update_location():
    data = request.json
    location_data['latitude'] = data.get('latitude')
    location_data['longitude'] = data.get('longitude')
    return jsonify({'message': 'Location updated successfully'}), 200

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(emergency_contacts), 200

@app.route('/location', methods=['GET'])
def get_location():
    return jsonify(location_data), 200

if __name__ == '__main__':
    app.run(debug=True)
