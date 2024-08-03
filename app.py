from flask import Flask, render_template, jsonify
import json

app = Flask(__name__, static_folder='static')

# Simulate a data retrieval function
def GetData(dataName):
    data = {
        'views': {'value': 1234, 'css': 'color: red;'},
        'stepcount': {'value': 5678, 'css': 'color: blue;'},
        'progress': {'value': 75, 'css': 'background-color: green;'}
    }
    return data.get(dataName, {'value': 'N/A', 'css': ''})

# Load screen configurations from JSON file
with open('config.json', 'r') as f:
    screen_configurations = json.load(f)

@app.route('/<screen>')
def display_screen(screen):
    return render_template('screen.html', screen=screen)

@app.route('/api/config/<screen>')
def get_config(screen):
    config = screen_configurations.get(screen, [])
    return jsonify(config)

@app.route('/api/data/<data>')
def get_data(data):
    return jsonify(GetData(data))

@app.route('/template/<template_name>')
def get_template(template_name):
    return render_template(f'{template_name}.html')

if __name__ == '__main__':
    app.run(debug=True)
