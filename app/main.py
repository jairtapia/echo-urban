from fastapi import FastAPI
from app.routers.users import user
from app.routers.drivers import Rdriver

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": 'ok'}

    
app.include_router(user.router)
app.include_router(Rdriver.router)




