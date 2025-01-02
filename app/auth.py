from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import APIrouter, HTTPException, stauts
from models import Users

SECRET_KEY="your_secret_key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINITES=30
#CREATE JWT token
def create_access_token(data: dict,expires_delta: timedelta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINITES)):
    to_encode=data.copy()
    expire=datetime.utcnow()+expires_delta
    to_encode.update({"exp":expire})
    return encode_jwt
#VERIFY THE JWT token
def verify_token(token: str):
    try:
        playload=jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        return playload
    except JWTError:
        return None
router=APIrouter()
#lOGIN ROUTER tTO ISSUE JWT
@router.post("/token")
async def login_for_access_token(user: Users):
    #todo check user if exist and validata password
    access_token=create_access_token(data={"sub":username})
    return {"access_token":access_token,"token_type":"bearer"}
def git_current_user():
    Users=verify_token(token)
    if Users is None:
        raise HTTPException(stauts_code=stauts.HTTP_401_UNAUTHORIZED,detail="Invaaild")
    return Users