import json
import requests
from api_helper import get_token as token
from credential import URL, HEADER, USER


class TestRegister
    def test_login(app):
        response = requests.post(URL["register"],
                                data = json.dumps({
                                    "email": USER["email"],
                                    "username": USER["username"],
                                    "password": USER["pass"],
                                    "recaptchaToken": token(USER["email"]),
                                    },
                                headers = HEADER['header']
                                )
        resp = response.json()
        print(resp)
        assert 200 == response.status_code, "You have BAD REQUEST"
        assert True == resp["is_murren_created"], "Account not created"
