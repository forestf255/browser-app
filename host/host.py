from flask import Flask, render_template, request

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

sensorData = {
    "sensor1": 0,
    "sensor2": 0,
    "sensor3": 0,
}


@app.route('/', methods=['GET', 'PUT'])
def index():
    if request.method == 'PUT':
        for k in sensorData.keys():
            if k in request.form:
                sensorData[k] = int(request.form[k])
        return render_template('table.html', **sensorData)
    else:
        return render_template('table.html', **sensorData)
