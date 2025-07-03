from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import pymongo
import os

# Load MongoDB URL from .env
load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")

# Setup MongoDB connection
client = pymongo.MongoClient(MONGO_URL)
db = client.test
collection = db['assignment_task']

# Create Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            form_data = {
                "name": request.form['name'],
                "email": request.form['email'],
                "message": request.form['message']
            }
            collection.insert_one(form_data)
            return redirect(url_for('success'))
        except Exception as e:
            return render_template('index.html', error=str(e))

    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
