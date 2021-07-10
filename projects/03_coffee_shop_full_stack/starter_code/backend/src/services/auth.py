import json
from flask import request, _request_ctx_stack
from functools import wraps
import jwt
from urllib.request import urlopen


AUTH0_DOMAIN = 'dev-test-coffee-shop.eu.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'dev'

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

def get_token_auth_header():
    auth_header = request.headers.get('Authorization', None)
    if not auth_header:
        raise AuthError('Authorization header is not present in request headers')
    
    auth_parts = auth_header.split(" ")
    if len(auth_parts) < 2:
        raise AuthError('Mailformed JWT Authorization header')
    
    return auth_parts[1]

'''
    it should raise an AuthError if permissions are not included in the payload
        !!NOTE check your RBAC settings in Auth0
    it should raise an AuthError if the requested permission string is not in the payload permissions array
    return true otherwise
'''
def check_permissions(permission, payload):
    raise Exception('Not Implemented')

def verify_decode_jwt(token):
    unverified_header = jwt.get_unverified_header(token)
    auth0_public_keys = json.load(urlopen("https://" + AUTH0_DOMAIN + "/.well-known/jwks.json").read())
    
    rsa_key = {}
    for key in auth0_public_keys["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }            

    if not rsa_key:
        raise AuthError('Cannot find valid RSA key')
    
    try:
        payload = jwt.decode(token, rsa_key, algorithms=ALGORITHMS, audience=API_AUDIENCE, issuer="https://"+AUTH0_DOMAIN+"/")
        print(payload)
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthError("Token is expired")
    except jwt.JWTClaimsError:
        raise AuthError("Invalid claims")
    except Exception:
        raise AuthError("Invalid authorization token")
        
'''
@TODO implement @requires_auth(permission) decorator method
    @INPUTS
        permission: string permission (i.e. 'post:drink')

    it should use the get_token_auth_header method to get the token
    it should use the verify_decode_jwt method to decode the jwt
    it should use the check_permissions method validate claims and check the requested permission
    return the decorator which passes the decoded payload to the decorated method
'''
def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator