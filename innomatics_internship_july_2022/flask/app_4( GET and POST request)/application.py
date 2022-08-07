
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def fun_1():
    if request.method == 'POST':
        email = request.form['in_1']
        return "Welcome {}".format(email)
    
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search_function():
    query = request.args['q'] 
    # to get access of the data in the front end we have to use request.args for get request and request.form for post request
    return "Search query entered : {}".format(query)

if __name__ == '__main__':
    app.run(debug=True)