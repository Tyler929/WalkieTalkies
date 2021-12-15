#import "packages" from flask
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


@app.route('/aboutus/')
def aboutus():
    return render_template("aboutus.html")

@app.route('/kaavya/',methods=['GET', 'POST'])
def kaavya():
    url = "https://quotes15.p.rapidapi.com/quotes/random/"

    headers = {
    'x-rapidapi-host': "quotes15.p.rapidapi.com",
    'x-rapidapi-key': "4bb3809bf7msh948c9bbf8c0eb81p114fecjsn20d2fe36897b"
    }

    response = requests.request("GET", url, headers=headers)
    return render_template("kaavya.html", quotes=response.json())
    print(response.text)

#@app.route('/kamya/')
#def kamya():
    #return render_template("kamya.html")

@app.route('/tyler/')
def tyler():
    return render_template('tyler.html')

@app.route('/design/')
def design():
    return render_template("design.html", padlet="https://padlet.com/kamya04mahendru/u2t64vrl8q6bjdic")


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

@app.route('/kamya/',methods=['GET', 'POST'])
def kamya():
    url = "https://random-words5.p.rapidapi.com/getMultipleRandom"

    querystring = {"count":"5"}

    headers = {
    'x-rapidapi-host': "random-words5.p.rapidapi.com",
    'x-rapidapi-key': "baf45032bdmsh1fb0709d81a2d0ep1d1bfejsnb09953cc9b71"
}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("kamya.html", word=response.json())
    print(response.text)

@app.route('/artists/')
def artists():
    return render_template('artists.html')

@app.route('/famous/')
def famous():
    return render_template('famous.html')
@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')
# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)

