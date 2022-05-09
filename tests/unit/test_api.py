import pytest
from ...nftapi import app
import json




def test_get_api():
    client = app.test_client()
    response = client.get('/byname?name=4893750493875')
    assert response.status_code == 200

def test_get_api_failure():
    client = app.test_client()
    response = client.post('/byname', query_string={'name': 'Cats'})
    assert response.status_code == 405