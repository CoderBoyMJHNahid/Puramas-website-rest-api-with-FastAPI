from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.eng_route import router as eng_router
from app.api.fr_route import router as fr_router
from app.api.de_route import router as de_router
from app.api.ar_route import router as ar_router
from app.api.cn_route import router as cn_router
from app.api.it_route import router as it_router


app = FastAPI()

origins = [
            "http://it.puramas.co",
            "https://it.puramas.co",
        ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(eng_router,prefix="/api/spa",tags=["posts"])
app.include_router(eng_router,prefix="/api/eng",tags=["posts"])
app.include_router(fr_router,prefix="/api/fr",tags=["posts"])
app.include_router(de_router,prefix="/api/de",tags=["posts"])
app.include_router(cn_router,prefix="/api/cn",tags=["posts"])
app.include_router(ar_router,prefix="/api/ar",tags=["posts"])
app.include_router(it_router,prefix="/api/it",tags=["posts"])



@app.get("/")
def root():
    return {"message":"Welcome to the api system"}
