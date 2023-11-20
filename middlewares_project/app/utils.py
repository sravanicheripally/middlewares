# myapp/utils.py

import jwt
from django.conf import settings
from django.contrib.auth.models import User
BLACKLISTED_TOKENS = set()
def create_tokens(user):
    access_payload = {
        'user_id': user.id,
        'username': user.username,
    }

    refresh_payload = {
        'user_id': user.id,
        'refresh': True,
    }

    access_token = jwt.encode(access_payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    refresh_token = jwt.encode(refresh_payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    return access_token, refresh_token

def verify_access_token(token):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        user_id = payload.get('user_id')
        return User.objects.get(id=user_id)
    except jwt.ExpiredSignatureError:
        # Handle token expiration
        return None
    except jwt.InvalidTokenError:
        # Handle invalid token
        return None

def verify_refresh_token(token):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        user_id = payload.get('user_id')
        if payload.get('refresh') and user_id:
            return User.objects.get(id=user_id)
    except jwt.ExpiredSignatureError:
        # Handle token expiration
        return None
    except jwt.InvalidTokenError:
        # Handle invalid token
        return None
