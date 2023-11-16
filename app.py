from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, from Docker! Testing the change.'

if __name__ == "__main__":
    #set debug = true for development env.
    app.run(host='0.0.0.0', port=5001)