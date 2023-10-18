import json  
from flask import Flask, request, redirect, url_for, render_template_string
import requests


app = Flask(__name__)

@app.route('process', methods=['POST'])
def process_data()
    data = request.json
    processed_data = {k v2 for k, v in data.items()}
    return jsonify(processed_data)

if __name__ == '__main__'
    app.run(host='0.0.0.0', port=5001)
