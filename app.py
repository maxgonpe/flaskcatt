from flask import Flask, render_template
from jinja2 import FileSystemLoader

app = Flask(__name__, template_folder='templates', static_folder='static')
app.jinja_loader = FileSystemLoader(app.template_folder)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()