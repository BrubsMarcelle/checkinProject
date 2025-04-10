from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.security import get_current_user
from app.api.user_routes import router as user_router
from app.api.chekin_routes import router as checkin_router
from app.api.ranking_routes import router as ranking_router
from app.api.alert_routes import router as alert_router

# Instância do FastAPI
app = FastAPI()

# Esquema de autenticação OAuth2 com Bearer Token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login", scheme_name="JWT")

# Incluir as rotas
app.include_router(user_router, prefix="/api")
app.include_router(checkin_router, prefix="/api")
app.include_router(ranking_router, prefix="/api")
app.include_router(alert_router, prefix="/api")

# Endpoint protegido de exemplo
@app.get("/secure-endpoint")
async def secure_endpoint(current_user: str = Depends(get_current_user)):
    return {"message": "You are authenticated", "user_id": current_user}

# Endpoint de boas-vindas
@app.get("/")
async def root():
    return {"message": "Welcome to the Cognitive Training API"}