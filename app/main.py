import os
import subprocess
from flask import Flask, request

app = Flask(__name__)

BASE_DIR = os.environ.get("BASE_DIR")
PBO_TOOL = os.environ.get("PBO_TOOL")

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.get_json()

    # Extract modified files from webhook payload
    modified_files = []
    for commit in data.get("commits", []):
        modified_files.extend(commit.get("added", []) + commit.get("modified", []))

    # Identify affected addon folders
    affected_addons = set()
    for file_path in modified_files:
        if file_path.startswith("jtf-main-pack/addons/"):
            folder = file_path.split("/")[2]
            affected_addons.add(folder)

    # PBO each affected addon
    for addon in affected_addons:
        addon_path = os.path.join(BASE_DIR, addon)
        if os.path.isdir(addon_path):
            pbo_path = f"{addon_path}.pbo"
            print(f"PBO'ing {addon}...")
            subprocess.run([PBO_TOOL, addon_path, pbo_path])

    return "Processed", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
