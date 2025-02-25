import requests
import pytest
from unittest import TestCase

url_user = "https://library-07f2.onrender.com/api/users"
url_auth = "https://library-07f2.onrender.com/api/auth"

def test_create_valid_admin_user():

    user = {
                "name": "Guille admin",
                "email": "gui2@gmail.com",
                "password": "12345",
                "isAdmin": "true"
            }
    
    response = requests.post(url_user, json = user)
    assert response.status_code == 200

    print(response.status_code)
    print(response.reason)


def test_authorization_user():
    user = {
	            "email": "gui2@gmail.com",
                "password": "12345"
            }

    response = requests.post(url_auth, json = user)
    token = response.content
    assert response.status_code == 200

    print(response.status_code)
    print(response.reason)   
    print(token)         


def test_get_all_genres():
    
    url = "https://library-07f2.onrender.com/api/genres"
    response = requests.get(url)
    assert response.status_code == 200


# def test_insert_post():

#     genre = {'name': 'biografia'}
#     response = requests.post(url, json = genre)


    
if __name__ == "__main__":

    #//400 - Bad request

    #test_get_all_genres()
    #test_create_valid_admin_user()
    test_authorization_user()

