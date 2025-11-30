from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Basic API is running!"}

@app.post("/upload")
async def upload(file: UploadFile):
    return {"message": "Upload route working", "filename": file.filename}

@app.get("/status")
def status():
    return {"message": "Status route working"}

@app.get("/download")
def download():
    return {"message": "Download route working"}
