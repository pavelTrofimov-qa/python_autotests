import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '7c76eb0af79e31f72a38296eed64b933'


def test_status_code():
    respons = requests.get(f'{host}/trainers', params = {"trainer_id": 3793})
    assert  respons.status_code == 200