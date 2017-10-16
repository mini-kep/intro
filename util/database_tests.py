"""Specification tests for deployed application. 

These tests are a quick check for "Does appliation generally fit the 
<spec_database.py> specification?"

These tests call http address of deployed apllication. They may be used to check
both flask and django application.
   
These tests DO NOT substitute internal unittests inside the application. 
The intenal tests should not call http, but rather use app.test_client()
in flask or similar command in django.

"""
import json

import requests

HOST = 'http://127.0.0.1:5000'
POST_URI = HOST + '/api/incoming'
BASE_URI = HOST + '/api/datapoints'

DATA = json.dumps([{'date': '2017-09-18', 'freq': 'd', 'name': 'BRENT', 'value': 55.5},
                   {'date': '2017-09-15', 'freq': 'd', 'name': 'BRENT', 'value': 56.18},
                   {'date': '2017-09-14', 'freq': 'd', 'name': 'BRENT', 'value': 56.76},
                   {'date': '2017-09-13', 'freq': 'd', 'name': 'BRENT', 'value': 55.52},
                   {'date': '2017-09-12', 'freq': 'd', 'name': 'BRENT', 'value': 55.06},
                   {'date': '2017-09-11', 'freq': 'd', 'name': 'BRENT', 'value': 54.2}]
)


class TestPOST():
    # success
    def test_posting_valid_data(self):
        """Return an empty JSON on success"""
        data = DATA
        headers = {'content-type': 'application/json'}
        response = requests.post(POST_URI, json=data, headers=headers)
        assert response.json() == []

    # fail
    def test_posting_nothing(self):
        """Results in a 400 error"""
        response = requests.post(POST_URI)
        # FIXME:'123qwe'
        assert response.status_code == '123qwe'



class TestGET():
    # happy paths
    def test_request_response_with_valid_params(self):
        """Completed successfully with OK status code"""
        payload = {'name': 'BRENT', 'freq': 'd'}
        response = requests.get(BASE_URI, params=payload)
        assert response.ok

    def test_getting_BRENT(self):
        """Return a list with items that have the requested variable"""
        payload = {
            'name': 'BRENT',
            'freq': 'd'
        }
        response = requests.get(BASE_URI, params=payload)
        assert response.json()[0]['name'] == 'BRENT'

    # sad paths
    def test_request_with_empty_name(self):
        """Return 400 error with empty name parameter"""
        payload = {'name': '', 'freq': 'm'}
        response = requests.get(BASE_URI, params=payload)
        assert response.status_code == 400

    def test_request_with_empty_frequency(self):
        """Return 400 error with empty freq parameter"""
        payload = {'name': 'BRENT', 'freq': ''}
        response = requests.get(BASE_URI, params=payload)
        assert response.status_code == 400

    def test_getting_data_not_found(self):
        """Return response with empty json"""
        payload = {'name': 'FOOBAR', 'freq': 'm'}
        response = requests.get(BASE_URI, params=payload)
        assert response.json() == []