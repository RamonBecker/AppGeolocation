import requests
from random import randint
# from django.conf import settings
from geo import settings
from django.contrib.gis.geoip2 import GeoIP2, GeoIP2Exception
import socket
from requests import get

YELP_SEARCH_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'


def yelp_search(keyword=None, location=None):
    # Keyword = palavra chave a ser buscada
    # location = cidade a ser buscada
    headers = {"Authorization": "Bearer " + settings.YELP_API_KEY}

    # Se a keyword e location existirem
    if keyword and location:
        params = {'term': keyword, 'location': location}
    # Se não, definimos parametros default para realizar a busca
    else:
        params = {'term': 'Pizzaria', 'location': 'Florianópolis'}

    # Realizando a requisição e autorização com o headers para a api
    r = requests.get(YELP_SEARCH_ENDPOINT, headers=headers, params=params)
    #print(r.json())
    return r.json()


def get_client_data():
    # função para retornar a cidade através de um IP
    g = GeoIP2()
    ip = get_random_ip()
    try:
        return g.city(ip)
    # Caso não for encontrado a cidade, é lançado a exceção e retornado None
    except GeoIP2Exception:
        return None

#Gerando ips randomicos para busca
def get_random_ip():
    return '.'.join([str(randint(0, 255)) for x in range(4)])


def buscar_cidade_atual():
    ip = get('https://api.ipify.org').text
    g = GeoIP2()

    try:
        return g.city(str(ip))
    # Caso não for encontrado a cidade, é lançado a exceção e retornado None
    except GeoIP2Exception:
        return None




    return str(ip_externo)