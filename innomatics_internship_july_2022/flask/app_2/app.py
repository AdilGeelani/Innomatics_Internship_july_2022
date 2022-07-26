#  we can also link a html page to a flask app

# import the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url

@app.route('/')
def home():
    return render_template('index.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
