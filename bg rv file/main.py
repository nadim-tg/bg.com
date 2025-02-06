from fastapi import FastAPI, File, UploadFile
import requests
from io import BytesIO
from starlette.responses import StreamingResponse

app = FastAPI()
API_KEY = "YPdDyUoAohCgLtqtrEndwTji"

@app.post("/remove-bg")
async def remove_bg(image: UploadFile = File(...)):
    headers = {"X-Api-Key": API_KEY}
    files = {"image_file": (image.filename, await image.read(), image.content_type)}
    response = requests.post("https://api.remove.bg/v1.0/removebg", headers=headers, files=files)
    
    if response.status_code == 200:
        return StreamingResponse(BytesIO(response.content), media_type="image/png")
    return {"error": "Failed to remove background"}
API_KEY = "YPdDyUoAohCgLtqtrEndwTji"
@app.post("/remove-bg")
async def remove_bg(image: UploadFile = File(...)):
    headers = {"X-Api-Key": API_KEY}
    files = {"image_file": (image.filename, await image.read(), image.content_type)}
    response = requests.post("https://api.remove.bg/v1.0/removebg", headers=headers, files=files)
    
    if response.status_code == 200:
        return StreamingResponse(BytesIO(response.content), media_type="image/png")
    
    return {"error": f"Failed to remove background. Status: {response.status_code}, Message: {response.text}"}
