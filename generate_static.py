import os
from flask import Flask, render_template

# Create a minimal Flask app instance
app = Flask(__name__, static_folder='static', template_folder='templates')

# Ensure the _site directory exists
output_dir = '_site'
os.makedirs(output_dir, exist_ok=True)

# Use app context to render templates
with app.app_context():
    # Render index.html
    rendered_index = render_template('index.html')
    with open(os.path.join(output_dir, 'index.html'), 'w') as f:
        f.write(rendered_index)

    # Render result.html (with placeholder data)
    rendered_result = render_template('result.html', prediction="", text="")
    with open(os.path.join(output_dir, 'result.html'), 'w') as f:
        f.write(rendered_result)

print(f"Static files generated in {output_dir}/")