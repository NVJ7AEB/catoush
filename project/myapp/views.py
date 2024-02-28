from django.shortcuts import render
from django.http import FileResponse, HttpResponseNotFound
import os

def serve_pdf(request, filename):
    pdf_path = os.path.join('question_papers', filename)
    if os.path.exists(pdf_path):
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    else:
        return HttpResponseNotFound('PDF file not found')


# Create your views here.
