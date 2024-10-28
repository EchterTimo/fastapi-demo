from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "it works"}


@app.get("/ip")
async def get_client_ip(request: Request):
    client_ip = request.client.host
    return {"ip": client_ip}
