from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from app.core.config import settings

# Esquema de autenticação Bearer Token
bearer_scheme = HTTPBearer()

def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Cria um token JWT com os dados fornecidos.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    """
    Verifica e decodifica um token JWT.
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token expirado
    except jwt.InvalidTokenError:
        return None  # Token inválido

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    """
    Extrai o user_id do token JWT.
    """
    try:
        token = credentials.credentials
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")