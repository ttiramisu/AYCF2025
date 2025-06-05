from flask import Flask, render_template
from vercel_wsgi import handle_request

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

# Vercel uses this to invoke your Flask app
def handler(environ, start_response):
    return handle_request(app, environ, start_response)
