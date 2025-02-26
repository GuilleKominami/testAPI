import requests
import pytest
from unittest import TestCase
import csv

url_user = "https://library-07f2.onrender.com/api/users"
url_auth = "https://library-07f2.onrender.com/api/auth"


def read_data_test(file_name):
    with open(file_name, newline='') as csvfile:
        
        #data_test = csv.reader(csvfile, delimiter=' ', quotechar='|')
        
        data_test_obj = csv.DictReader(csvfile) 

        for row in data_test_obj:
            print(row["description"])


def test_api_with_multiple_inputs():
    inputs = [
        {"data": "validData", "expected_status": 200},
        {"data": "", "expected_status": 400},
        {"data": "edgeCaseData", "expected_status": 202}
    ]
    for input in user_inputs:
        response = requests.post("<http://api.endpoint>", data=input["data"])
        assert response.status_code == input["expected_status"]

def test_create_valid_admin_user():

    user = {
                "name": "Guille admin",
                "email": "gui2@gmail.com",
                "password": "12345",
                "isAdmin": "true"
            }
    
    for input in user_inputs:
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
    #test_authorization_user()

    read_data_test("data_user.csv")

