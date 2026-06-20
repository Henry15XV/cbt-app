import os

# Create the project directory
project_dir = "/mnt/agents/output/cbt_app"
os.makedirs(project_dir, exist_ok=True)

# Create app.py - the main Flask application
app_py = '''from flask import Flask, render_template, request, jsonify, session
import json
import os
from datetime import datetime

app = Flask(name)
app.secret_key = 'your-secret-key-change-this-in-production'

# CBT Questions
CBT_QUESTIONS = [
    {
        "id": 1,
        "question": "What situation triggered your negative thoughts?",
        "type": "text",
        "placeholder": "Describe what happened..."
    },
    {
        "id": 2,
        "question": "What negative thoughts went through your mind?",
        "type": "text",
        "placeholder": "I thought..."
    },
    {
        "id": 3,
        "question": "What emotions did you feel? (Rate 0-10)",
        "type": "scale",
        "emotions": ["Anxiety", "Sadness", "Anger", "Guilt", "Shame"]
    },
    {
        "id": 4,
        "question": "What evidence supports these negative thoughts?",
        "type": "text",
        "placeholder": "Facts that support the thought..."
    },
    {
        "id": 5,
        "question": "What evidence contradicts these negative thoughts?",
        "type": "text",
        "placeholder": "Facts that go against the thought..."
    },
    {
        "id": 6,
        "question": "What would you tell a friend in this situation?",
        "type": "text",
        "placeholder": "Be compassionate..."
    },
    {
        "id": 7,
        "question": "What is a more balanced thought?",
        "type": "text",
        "placeholder": "A realistic perspective..."
    },
    {
        "id": 8,
        "question": "How do you feel now? (Rate 0-10)",
        "type": "scale",
        "emotions": ["Anxiety", "Sadness", "Anger", "Guilt", "Shame"]
    }
]

@app.route('/')
def index():
    return render_template('index.html', questions=CBT_QUESTIONS)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    
    # Save response with timestamp
    response = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'answers': data
    }
    
    # Store in session (in production, use a database)
    if 'responses' not in session:
        session['responses'] = []
    session['responses'].append(response)
    session.modified = True
    
    return jsonify({'status': 'success', 'message': 'Responses saved successfully!'})

@app.route('/results')
def results():
    responses = session.get('responses', [])
    return render_template('results.html', responses=responses)

@app.route('/clear', methods=['POST'])
def clear():
    session.pop('responses', None)
    return jsonify({'status': 'success', 'message': 'All responses cleared!'})

if name == 'main':
    app.run(debug=True, host='0.0.0.0', port=5000)
'''

with open(os.path.join(project_dir, "app.py"), "w") as f:
    f.write(app_py)

print("✅ app.py created")
