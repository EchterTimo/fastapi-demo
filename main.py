from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/public-ip")
async def get_public_ip():
    # Use an external service to get the public IP
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.ipify.org?format=json')
        return response.json()  # Returns {"ip": "your_public_ip"}
