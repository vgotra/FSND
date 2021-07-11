import json
from flask import request, _request_ctx_stack
from functools import wraps
from urllib.request import urlopen
from jose import jwt
from errors.AuthError import AuthError


AUTH0_DOMAIN = 'dev-test-coffee-shop.eu.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'https://coffee-shop-api'


def get_token_auth_header():
    auth_header = request.headers.get('Authorization', None)
    if not auth_header:
        raise AuthError(
            'Authorization header is not present in request headers', 401)

    auth_parts = auth_header.split(" ")
    if len(auth_parts) < 2:
        raise AuthError('Mailformed JWT Authorization header', 401)

    return auth_parts[1]


def check_permissions(permission, payload):
    if not (payload["permissions"]):
        raise AuthError('No permissions', 401)
    if not permission in payload["permissions"]:
        raise AuthError("Permissions error", 401)
    return True


def verify_decode_jwt(token):
    unverified_header = jwt.get_unverified_header(token)
    response = urlopen(
        "https://" +
        AUTH0_DOMAIN +
        "/.well-known/jwks.json").read()
    auth0_public_keys = json.loads(response.decode('utf-8'))

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
        raise AuthError('Cannot find valid RSA key', 401)

    try:
        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=ALGORITHMS,
            audience=API_AUDIENCE,
            issuer="https://" +
            AUTH0_DOMAIN +
            "/")
        _request_ctx_stack.top.current_user = payload
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthError("Token is expired", 401)
    except jwt.JWTClaimsError:
        raise AuthError("Invalid claims", 401)
    except Exception:
        raise AuthError("Invalid authorization token", 401)


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(*args, **kwargs)
        return wrapper
    return requires_auth_decorator
