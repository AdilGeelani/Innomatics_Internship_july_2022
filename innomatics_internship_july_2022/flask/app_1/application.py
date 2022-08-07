# import the librabry
from flask import Flask 


# instantiate the app
app = Flask(__name__)


# make a route and link it to the function
@app.route('/')
def index():
    return "Hello World"


# run the app
if __name__ == "__main__":
    app.run(debug=True) # runs the app in debug mode