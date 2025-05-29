from flask import Flask, render_template_string

# Create a Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template_string('''
        <h1>Welcome to My Flask App!</h1>
        <p>Try these links:</p>
        <ul>
            <li><a href="/hello">Hello Page</a></li>
            <li><a href="/greet/YourName">Greet Page</a></li>
        </ul>
    ''')

# Define a route for a simple hello page
@app.route('/hello')
def hello():
    return "<h2>Hello, World!</h2><p>This is a simple Flask route.</p>"

# Define a route with a variable
@app.route('/greet/<name>')
def greet(name):
    return render_template_string('''
        <h2>Hello, {{ name }}!</h2>
        <p>Nice to meet you.</p>
        <a href="/">Back to Home</a>
    ''', name=name)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
