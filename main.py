from flask import Flask, render_template, request
from __init__ import app
import requests
from image import image_data
#from crud.app_crud import app_crud
from pathlib import Path



#app.register_blueprint(app_crud)

# connects default URL to render tictactoe.html
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

@app.route('/graph/')
def graph():
    return render_template('graph.html')

@app.route('/artgame/')
def artgame():
    return render_template('artgame.html')

@app.route('/famous/')
def famous():
    return render_template('famous.html')

@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')

@app.route('/artquiz/')
def artquiz():
    return render_template('artquiz.html')

@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/locationfinder/')
def locationfinder():
    return render_template('locationfinder.html')



@app.route('/palindrome/')
def palindrome():
    return render_template('palindrome.html')

@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    path = Path(app.root_path) / "static" / "rgb"
    return render_template('rgb.html', images=image_data(path))

@app.route('/tyler/',methods=['GET', 'POST'])
def tyler():
    url = "https://random-facts2.p.rapidapi.com/getfact"
    headers = {
    'x-rapidapi-host': "random-facts2.p.rapidapi.com",
    'x-rapidapi-key': "cc605079ecmshde1003394962679p1f03aejsn9e04c36c03b8"
    }

    response = requests.request("GET", url, headers=headers)

    return render_template("tyler.html", facts=response.json())
    print(response.text)


@app.route('/faq/')
def faq():
    return render_template('faq.html')


@app.route('/art', methods=['GET', 'POST'])
def art():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/art"
    """
    url = "https://walkietalkies.cf/api/art"

    response = requests.request("GET", url)
    return render_template("artapi.html", arts=response.json())

@app.route('/artquiz/')
def artquiz():
    return render_template('artquiz.html')


@app.route('/ImageAPI/')
def imageapi():
    return render_template('ImageAPI.html')


@app.route('/pong/')
def pong():
    return render_template("pong.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)

