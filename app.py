from flask import Flask, request, jsonify
app = Flask(__name__)

# python -m flask run
# ctrl + click: http://127.0.0.1:5000/

#'''
@app.route('/')
def index():
    # Read the content of index.html and return it
    with open('index.html', 'r') as file:
        content = file.read()
    return content

#'''

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    
    # Assuming the file contains text
    content = uploaded_file.read().decode('utf-8')
    
    # Processing the file to generate a score (simplified)
    score = len(content.split())  # Score based on word count
    
    return jsonify({'score': score})
#'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)