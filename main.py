from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
    Base function for now
    :return:
    """
    # test
    return {"message": "Hello World"}
