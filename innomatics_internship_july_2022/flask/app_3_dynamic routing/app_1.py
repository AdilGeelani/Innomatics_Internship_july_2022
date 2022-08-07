# dynamic routing is a way to create a URL that can be changed at runtime. so we dont need to make a route for each entry
from flask import Flask, render_template

# create an instance of the Flask class
app = Flask(__name__)

# create a route for the root of the site
@app.route('/')
def index():
    return 'Welcome to the home page'

@app.route('/user/<user_name>')  # dynamic routing so we have to run the url 127.0.0.1:5000/user/<user_name> to see the output
# user_name is a variable that can be used in the template and keepson updating
def user_profile(user_name):
    return "Welcome {}!".format(user_name)

if __name__ == "__main__":
    app.run(debug=True)


