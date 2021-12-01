# import "packages" from flask
from flask import Flask, render_template, request
import requests

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/greet/')
def greet():
    return render_template("greet.html")

@app.route('/katie', methods=['GET', 'POST'])
def katie():
    url = "https://numbersapi.p.rapidapi.com/random/trivia"

    querystring = {"min":"1","max":"100","fragment":"true","json":"true"}

    headers = {
        'x-rapidapi-host': "numbersapi.p.rapidapi.com",
        'x-rapidapi-key': "fae3fd2dd7mshb51665dc058f9ecp12ba4djsn73ae03643dfa"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("katie.html", numbers=response.json())
    print(response.text)

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)

