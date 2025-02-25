import requests
import pytest
from unittest import TestCase

def test_create_valid_admin_user():

    url = "https://library-07f2.onrender.com/api/users"
    user = {
                "name": "Guille admin",
                "email": "gui1@gmail.com",
                "password": "1234",
                "isAdmin": "true"
            }
    
    response = requests.post(url, json = user)
    print(response.status_code)
    print(response.reason)
    #assert response.status_code == 200

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
    test_create_valid_admin_user()

