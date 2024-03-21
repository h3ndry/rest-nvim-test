import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():

    x = 0

    for y in range(0, 10):
        x = +y

    return {"message": "Hello World", "xy": x}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
