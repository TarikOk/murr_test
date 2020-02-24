import json
import requests
import pytest
from api_helper import get_token as token
from credential import URL, HEADER, USER


def test_login(app):
    response = requests.post(URL["url"]+URL["register"],
                            data = json.dumps({
                                "email": USER["email"],
                                "username": USER["username"],
                                "password": USER["pass"],
                                "recaptchaToken": token(USER["email"])
                                })
                            )
    resp = response.json()
    print(resp)
    print(token(USER["email"]))
    assert 200 == response.status_code, "You have BAD REQUEST"
    assert "true" == resp["is_murren_created"]
