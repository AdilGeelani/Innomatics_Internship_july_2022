from flask import Flask

app = Flask(__name__)
registered_users = ["adil", "irfan", "farhan"]
@app.route('/')
def index():
    return 'Welcome to the home page'

@app.route('/user/<user_name>')  # dynamic routing so we have to run the url
# user_name is a variable that can be used in the template and keepson updating
def user_profile(user_name):
    # we can also use condition to give access to some users only
    if user_name in registered_users:
        return "Welcome {}!".format(user_name)
    else:
        return "User not found. Please register"

if __name__ == "__main__":
    app.run(debug=True)
