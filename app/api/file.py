import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from app import app

from google.cloud import storage
from app.GCP.googleStorage import GoogleStorage


@app.route('/api/file', methods=['POST'])
def api_file_post():
    google_storage = GoogleStorage('thehut')
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    file.filename = secure_filename(file.filename)

    return google_storage.upload_file(
        file.read(),
        file.filename,
        file.content_type
    )
