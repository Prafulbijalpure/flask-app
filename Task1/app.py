from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api')
def api():
    # Step 1: Open the file and read the content
    with open('data.txt', 'r') as file:
        data = file.read()
    
    # Step 2: Convert the text data into a Python list
    json_data = json.loads(data)

    # Step 3: Send it back as JSON response
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)
