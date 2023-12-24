from flask import Flask, render_template, request, jsonify, send_file
from models.generatecourses import process
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/samplepdf', methods=['GET', 'POST'])
def download_sample_pdf():
    # Provide the correct path to your sample_agreement.pdf file
    sample_pdf_path = 'sample_agreement.pdf'

    # Check if the file exists
    if os.path.exists(sample_pdf_path):
        return send_file(sample_pdf_path, as_attachment=True)
    else:
        return "Sample PDF not found", 404
    
    
@app.route('/generate', methods=['POST', 'GET'])
def generate():
    try:
        # Get data from the request
        pdf_file = request.files.get('pdfFile')
        qmax = int(request.form.get('qmax'))
        smax = int(request.form.get('smax'))
        print(qmax, smax, "values")
        interests = request.form.getlist('interests[]')
        print(interests, "interests", type(interests))
        # Check if a file is provided
        if not pdf_file:
            return jsonify(error="Please upload a PDF file."), 400

        # Read the content of the PDF file
        pdf_data = pdf_file.read()

        # Call the process function
        result = process(pdf_data, qmax, smax, interests)
        # Return the result
        return jsonify(result)

    except Exception as e:
        # Handle exceptions appropriately
        print(f"Error generating schedule: {str(e)}")
        return jsonify(error="Error generating schedule. Please try again."), 500

if __name__ == '__main__':
    app.run(debug=True)
