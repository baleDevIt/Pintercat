from enum import Enum

url_ricerca = "https://api.thecatapi.com/v1/images/search?"
url_breeds = "https://api.thecatapi.com/v1/breeds"


class SearchParameter(Enum):
    LIMIT = "limit="
    ORDER = "order="
    ID_CATEGORY = "category_ids="
    BREED = "breed_ids="
    HAS_BREAD = "has_breeds="



def getUrlSingleImage(id : str):
    return "https://api.thecatapi.com/v1/images/" + id
