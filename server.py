from bottle import Bottle, request, response, run

mem_slot = 3

app = Bottle()


@app.post("/uploadtmats")
def upload_tmats():
    # Get the uploaded file
    uploaded_file = request.files.get("upload")
    content_length = request.content_length
    if not content_length:
        content_length = 0

    if uploaded_file:
        # Save the uploaded file to the server (e.g., to /tmp directory)
        file_path = f"/tmp/{uploaded_file.filename}"
        uploaded_file.save(file_path)

        return ""


if __name__ == "__main__":
    # Run the server on port
    run(app, host="localhost", port=8100 + mem_slot)
