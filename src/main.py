from fastapi import FastAPI
from .routers import campaign
from .database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(campaign.router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
