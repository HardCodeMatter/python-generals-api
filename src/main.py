import uvicorn
from fastapi import FastAPI, APIRouter

from database import Base, engine
from routers import user as UserRouter


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='General Game API',
    version='0.1.0',
)
app.include_router(UserRouter.router, prefix='/user')

if __name__ == '__main__':
    uvicorn.run(
        'main:app', 
        host='0.0.0.0', 
        port=8080, 
        reload=True, 
        workers=3
    )
