import json
import requests
import pytest
from api_helper import get_token as token
from credential import URL, HEADER, USER


def test_resetpass(app):
    response = requests.post(URL["url"]+URL["reset_pass"],
                            data = json.dumps({
                                "email": USER["email"],
                                "recaptchaToken": token(USER["email"])
                                }),
                            headers = HEADER["header"]
                            )
    resp = response.json()
    assert 200 == response.status_code, "You have BAD REQUEST"
    assert resp["email_sent_successfully"]
