from fastapi import FastAPI, UploadFile,File

from services.merge import Merge
from PyPDF2 import PdfMerger
import io
from fastapi.responses import FileResponse
import tempfile
app=FastAPI()

@app.get('/')
async def base():
    return "Pdf_Pro: A pdf merge and spliting platform"


@app.post('/services/merge')
async def merge(files: list[UploadFile]):
    merger = PdfMerger()
    for file in files:
        pdf_file = await file.read()
        merger.append(io.BytesIO(pdf_file))

    merged_pdf = io.BytesIO()
    merger.write(merged_pdf)
    merger.close()

    # Save the merged PDF to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(merged_pdf.getvalue())
        temp_file_path = temp_file.name

    return FileResponse(temp_file_path, filename="merged.pdf", media_type="application/pdf")


@app.post('/services/split')
async def split(files:list[UploadFile],start_page:int=0,end_page:int =None):
    return True