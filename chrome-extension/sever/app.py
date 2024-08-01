import os
from flask import Flask, request, jsonify, render_template
import requests
import json

# Lấy đường dẫn tuyệt đối tới thư mục hiện tại
base_dir = os.path.dirname(os.path.abspath(__file__))

# Chỉ định thư mục chứa templates là 'html'
app = Flask(__name__, template_folder=os.path.join(base_dir, '../html'))

# URL cơ bản của API
base_url = 'https://66abb708636a4840d7cbad7d.mockapi.io/actions'

@app.route('/api/action', methods=['POST'])
def handle_action():
    data = request.get_json()
    platform = data['platform']
    action = data['action']
    content = data['content']
    
    # Dữ liệu để gửi tới MockAPI
    payload = {
        "platform": platform,
        "action": action,
        "content": content
    }
    
    # Thực hiện yêu cầu POST tới MockAPI
    response = requests.post(base_url, json=payload)
    
    if response.status_code == 201:
        return jsonify({"status": "success", "data": response.json()}), 201
    else:
        return jsonify({"status": "error", "message": response.text}), response.status_code

@app.route('/')
def index():
    return render_template('popup.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
