from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_json():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part', 400

        file = request.files['file']
        if file.filename == '':
            return 'No selected file', 400
        if file:
            file.save(file.filename)
            return 'File uploaded successfully'
    
    return 'Invalid request', 400

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
