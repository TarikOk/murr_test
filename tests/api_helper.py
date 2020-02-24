import requests
import credential
import jwt


def get_token(login):
    token = jwt.encode({'email': login}, "secret_key", algorithm='HS256').decode('utf-8')
    return token
