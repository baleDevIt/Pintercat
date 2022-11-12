from flask import Flask, render_template, request
from utility import SearchParameter, getUrlSingleImage, url_breeds, url_ricerca, url_search_single_cat
import requests
app = Flask(__name__)

allBreed = requests.get(url_breeds).json()


@app.route("/")
def index():
    # Instanzio variabili necessarie
    listCardCatHome = []
    params = ""
    for key in request.args.keys():
        params += "&"+ key + "=" + request.args.get(key)
    listCard = requests.get(url_ricerca + SearchParameter.LIMIT.value + str(10) + params).json()
    for card in listCard:
        listCardCatHome.append(requests.get(url_search_single_cat + card["id"]).json())
    return render_template('index.html', listCard = listCard, homePageBreed = allBreed, listCardCatHome = listCardCatHome)


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
    listCardSameId = []
    card = requests.get(url_search_single_cat + id).json()
    listCardSameId = requests.get(url_ricerca + SearchParameter.LIMIT.value + str(10)+ "&" + SearchParameter.BREED.value + card['breeds'][0]['id']).json()
    return render_template('post.html', card = card, listCardSameId = listCardSameId)
