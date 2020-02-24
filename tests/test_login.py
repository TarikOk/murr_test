import json
import requests
import pytest
from credential import URL, HEADER, USER


def test_login(app):
    response = requests.post(URL["url"]+URL["login"],
                            data = json.dumps({
                                "username": USER["username"],
                                "password": USER["pass"]
                                }),
                            headers = HEADER["header"]
                            )
    resp = response.json()
    if "refresh" in resp:
        val = True
    else:
        val = False
    assert 200 == response.status_code, "You have BAD REQUEST"
    assert True == val
