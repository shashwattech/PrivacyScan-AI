from flask import Flask, send_from_directory, request, jsonify
import subprocess
import os

app = Flask(__name__)

# Serve the index.html file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Endpoint to handle local scan request
@app.route('/scan_local', methods=['POST'])
def scan_local():
    local_path = request.json.get('local_path')
    if local_path:
        # Run DownloadRepo.py script
        result = subprocess.run(['python3', 'DownloadRepo.py', local_path], capture_output=True, text=True)
        if result.returncode == 0:
            # Run ReadDataUpdated.py script
            result = subprocess.run(['python3', 'ReadDataUpdated.py', local_path], capture_output=True, text=True)
            return jsonify({'status': 'success', 'output': result.stdout})
        else:
            return jsonify({'status': 'error', 'output': result.stderr}), 500
    return jsonify({'status': 'error', 'message': 'No local path provided'}), 400

# Endpoint to handle GitHub scan request
@app.route('/scan_github', methods=['POST'])
def scan_github():
    github_url = request.json.get('github_url')
    if github_url:
        # Run DownloadRepo.py script
        result = subprocess.run(['python3', 'DownloadRepo.py', github_url], capture_output=True, text=True)
        if result.returncode == 0:
            # Run ReadDataUpdated.py script
            local_path = "/Users/ssrivastava4/Desktop/PrivacyScan AI/Repo3"  # Update this path if necessary
            result = subprocess.run(['python3', 'ReadDataUpdated.py', local_path], capture_output=True, text=True)
            return jsonify({'status': 'success', 'output': result.stdout})
        else:
            return jsonify({'status': 'error', 'output': result.stderr}), 500
    return jsonify({'status': 'error', 'message': 'No GitHub URL provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
