from fastapi import FastAPI, File, UploadFile
import pandas as pd
from io import BytesIO

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}


# REQUIRED_COLUMNS = ["CUSTOMER NAME", "CORE_SYSTEM_CUSTID", "RM ID","RM","RM Mob. No."] 
# @app.post("/upload-xlsx/")
# async def extract_data(file: UploadFile = File(...)):
#     contents = await file.read()
#     df = pd.read_excel(BytesIO(contents))

 
#     missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
#     if missing_columns:
#         return {"error": f"Missing columns: {missing_columns}"}

#     extracted_data = df[REQUIRED_COLUMNS].to_dict(orient="records")
#     return extracted_data