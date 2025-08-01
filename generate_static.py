import os
import shutil
from flask import Flask, render_template, request

# Create a minimal Flask app instance
app = Flask(__name__, static_folder='static', template_folder='templates')

# Configure app for URL generation outside of request context
app.config['SERVER_NAME'] = 'example.com'
app.config['APPLICATION_ROOT'] = '/'
app.config['PREFERRED_URL_SCHEME'] = 'https'

# Register the same routes as in app.py to make url_for work
@app.route('/')
def home():
    return ""

@app.route('/predict', methods=['POST'])
def predict():
    return ""

# Ensure the _site directory exists
output_dir = '_site'
os.makedirs(output_dir, exist_ok=True)

# Use app context and test request context to render templates
with app.app_context():
    with app.test_request_context():
        # Render index.html
        rendered_index = render_template('index.html')
        with open(os.path.join(output_dir, 'index.html'), 'w') as f:
            f.write(rendered_index)

        # Render result.html (with placeholder data)
        rendered_result = render_template('result.html', prediction="", text="")
        with open(os.path.join(output_dir, 'result.html'), 'w') as f:
            f.write(rendered_result)
            
    # Copy static files to _site/static
    if os.path.exists('static'):
        static_output_dir = os.path.join(output_dir, 'static')
        if os.path.exists(static_output_dir):
            shutil.rmtree(static_output_dir)
        shutil.copytree('static', static_output_dir)

print(f"Static files generated in {output_dir}/")