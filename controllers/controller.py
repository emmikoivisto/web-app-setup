from app import app

@app.route('/')
def index():
    return "Hedgehogs rule"

@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"