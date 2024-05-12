from flask import Flask, jsonify, request
import xml.etree.ElementTree as ET
from global_var import *
from malware import *
from machine import *

app = Flask(__name__)

# api ssh
@app.route('/scan', methods=['POST'])
def _scan():
    fileName = request.json['data']
    scan(fileName)
    
    data = {
        'data':getMalwareFile()
    }

    return jsonify(data)

@app.route('/analyze', methods=['GET'])
def _analyze():
    deleteFile(SQLI_FILE)
    deleteFile(XSS_FILE)
    deleteFile(CMDI_FILE)
    deleteFile(PATH_TRAVERSAL)
    analyze()
    return jsonify({'data':'success'})

@app.route('/sqli', methods=['GET'])
def sqli():
    lines = readFile(SQLI_FILE)
    return jsonify({'logs':lines})

@app.route('/xss', methods=['GET'])
def xss():
    lines = readFile(XSS_FILE)
    return jsonify({'logs':lines})

@app.route('/cmdi', methods=['GET'])
def cmdi():
    lines = readFile(CMDI_FILE)
    return jsonify({'logs':lines})

@app.route('/path-traversal', methods=['GET'])
def pathTraversal():
    lines = readFile(PATH_TRAVERSAL)
    return jsonify({'logs':lines})




def readFile(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())  # Loại bỏ ký tự xuống dòng (\n) nếu cần
    return lines

def deleteFile(file_path):
    with open(file_path, 'w') as file:
        file.truncate(0)


if __name__ == '__main__':
    # subprocess.run(['sqlmapapi', '-s', '-H', '127.0.0.1', '-p', '7000'], check=True)
    compileRules()
    train()
    app.run(debug=True)