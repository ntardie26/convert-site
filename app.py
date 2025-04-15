from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

def hex_to_decimal(hex_string):
    return int(hex_string, 16)

def decimal_to_hex(decimal):
    return hex(int(decimal))[2:].upper()

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    binary = binary.replace(' ', '')
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8) if i+8 <= len(binary))

def decimal_to_binary(decimal):
    return bin(int(decimal))[2:]

def binary_to_decimal(binary):
    return int(binary, 2)

def hex_to_binary(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)

def binary_to_hex(binary):
    decimal = int(binary, 2)
    return hex(decimal)[2:].upper()

def text_to_hex(text):
    return ''.join(format(ord(char), '02X') for char in text)

def hex_to_text(hex_string):
    try:
        hex_string = hex_string.replace(' ', '')
        return bytes.fromhex(hex_string).decode('utf-8')
    except:
        return "Invalid hex input"

def text_to_decimal(text):
    return ' '.join(str(ord(char)) for char in text)

def decimal_to_text(decimal):
    try:
        values = decimal.strip().split()
        return ''.join(chr(int(value)) for value in values)
    except:
        return "Invalid decimal input"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    input_text = request.form.get('input_text', '')
    from_format = request.form.get('from_format')
    to_format = request.form.get('to_format')
    result = ''
    
    try:
        if from_format == 'hex':
            if to_format == 'decimal': result = str(hex_to_decimal(input_text))
            elif to_format == 'binary': result = hex_to_binary(input_text)
            elif to_format == 'text': result = hex_to_text(input_text)
        elif from_format == 'decimal':
            if to_format == 'hex': result = decimal_to_hex(input_text)
            elif to_format == 'binary': result = decimal_to_binary(input_text)
            elif to_format == 'text': result = decimal_to_text(input_text)
        elif from_format == 'binary':
            if to_format == 'hex': result = binary_to_hex(input_text)
            elif to_format == 'decimal': result = str(binary_to_decimal(input_text))
            elif to_format == 'text': result = binary_to_text(input_text)
        elif from_format == 'text':
            if to_format == 'hex': result = text_to_hex(input_text)
            elif to_format == 'decimal': result = text_to_decimal(input_text)
            elif to_format == 'binary': result = text_to_binary(input_text)
    except Exception as e:
        result = f"Error: {str(e)}"
    
    return jsonify({'result': result})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
