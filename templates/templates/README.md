import os

project_dir = "/mnt/agents/output/cbt_app"

# Check if README.md exists
readme_path = os.path.join(project_dir, "README.md")
print(f"README.md exists: {os.path.exists(readme_path)}")

# Recreate README.md
readme = '''# 🧠 CBT Thought Record App

A simple web-based Cognitive Behavioral Therapy (CBT) thought record application built with Python and Flask.

## Features

- ✅ Answer CBT questions about your thoughts and emotions
- ✅ Rate your emotions on a scale of 0-10
- ✅ Save your responses and review them later
- ✅ Beautiful, responsive design that works on mobile and desktop
- ✅ Share the link with friends so they can use it too

## How to Use

1. Visit the app URL
2. Fill out the CBT thought record questions
3. Click "Save My Responses"
4. View your past responses by clicking "View Past Responses"

## Technology Stack

- Python 3.11+
- Flask (web framework)
- HTML/CSS/JavaScript (frontend)
- Gunicorn (WSGI server for production)

## Local Development

1. Install dependencies:
  
   pip install -r requirements.txt
   
2. Run the app:
  
   python app.py
   
3. Open your browser and go to http://localhost:5000

## Deployment on Render

1. Push this code to a GitHub repository
2. Go to [render.com](https://render.com) and sign up
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Set the following:
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app:app
6. Click "Create Web Service"
7. Wait for deployment and get your URL!

## File Structure

cbt_app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Procfile           # Render deployment config
├── README.md          # This file
└── templates/
    ├── index.html     # Main CBT form page
    └── results.html   # View past responses page
## Note

This app uses Flask's built-in session storage. For production use with many users, consider adding a database like PostgreSQL or SQLite.
'''

with open(readme_path, "w") as f:
    f.write(readme)

print(f"✅ README.md created at: {readme_path}")
print(f"📄 Size: {os.path.getsize(readme_path)} bytes")

# Re-zip the project with README.md included
import zipfile

zip_path = "/mnt/agents/output/cbt_app.zip"

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, os.path.dirname(project_dir))
            zipf.write(file_path, arcname)

print(f"✅ Project re-zipped: {zip_path}")
print(f"📦 Size: {os.path.getsize(zip_path) / 1024:.1f} KB")

# List all files to confirm
print("\n📁 All files in project:")
for root, dirs, files in os.walk(project_dir):
    level = root.replace(project_dir, '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f'{subindent}{file}')
