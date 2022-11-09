from flask import Flask, render_template, request
from utility import SearchParameter, getUrlSingleImage, url_breeds, url_ricerca
import requests
app = Flask(__name__)

allBreed = requests.get(url_breeds).json()


@app.route("/")
def index():
    # Instanzio variabili necessarie
    listCard = []
    params = ""

    #Creo parte url dei parametri se presenti
    for key in request.args.keys():
        params += "&"+ key + "=" + request.args.get(key)

    #Effettuo chiamata e recupero il risultato della chiamata
    listCard = requests.get(url_ricerca + SearchParameter.LIMIT.value + str(10) + params).json()
    print(url_ricerca + SearchParameter.LIMIT.value + str(10) + params)

    #Passo tutto al render template
    return render_template('index.html', listCard = listCard, homePageBreed = allBreed)


@app.route("/login")
def loginIndex():
    pass

@app.route("/user")
def user():
    pass

@app.route("/author")
def getHomePageAuthor():
    return render_template('author.html')

@app.route("/post/<id>")
def getPost(id):
    return render_template('post.html')
