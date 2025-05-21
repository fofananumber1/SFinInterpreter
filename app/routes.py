from fastapi import APIRouter, UploadFile, File
import pandas as pd
from io import StringIO

router = APIRouter()

@router.get("/")
def root():
    return {"Message": "SFin is currently running"}

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        return {"error": "Only CSV files are supported."}
    
    contents = await file.read()
    decoded = contents.decode("utf-8")
    df = pd.read_csv(StringIO(decoded))

    # For now, just return the number of rows and columns
    return {
        "filename": file.filename,
        "rows": df.shape[0],
        "columns": df.shape[1],
        "preview": df.head(5).to_dict(orient="records")
    }