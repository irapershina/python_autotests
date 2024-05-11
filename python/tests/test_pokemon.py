import requests
import pytest

URL = 'https://pokemonbattle.me'
HEADER = {'Content-Type': 'application/json'}

def test_get_trainers():
    """
    KTI-1. Get trainers
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 3641}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'
    assert response.json()['name'] =='Homelander'