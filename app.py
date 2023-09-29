from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route and its handler function
@app.route('/')
def hello_world():
    return 'Hello, Community!'

if __name__ == '__main__':
    # Run the app on localhost, port 5000
    app.run(host='0.0.0.0', port=5000,debug=True)
