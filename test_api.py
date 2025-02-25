import requests
import pytest
from unittest import TestCase

url = "https://library-07f2.onrender.com/api/genres"

def test_get_all_genres():

    response = requests.get(url)
    print(response)
    assert response.status_code == 200


if __name__ == "__main__":
    
    test_get_all_genres()

