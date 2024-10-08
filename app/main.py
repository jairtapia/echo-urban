from fastapi import FastAPI
from app.routers.users.user import user

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": 'ok'}

    
app.include_router(user.router)




