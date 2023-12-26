import uvicorn
from fastapi import FastAPI

from database import Base, engine
from routers import user as UserRouter
from routers import property as PropertyRouter


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='General Game API',
    version='0.1.1',
)
app.include_router(UserRouter.router, prefix='/user')
app.include_router(PropertyRouter.router, prefix='/property')

if __name__ == '__main__':
    uvicorn.run(
        'main:app', 
        host='0.0.0.0', 
        port=8080, 
        reload=True, 
        workers=3
    )
