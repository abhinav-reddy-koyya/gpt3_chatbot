from flask import Flask, render_template, request, jsonify
import openai
import os
from PIL import Image
import pytesseract

app = Flask(__name__)
openai.api_key = "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"  # Replace with your real key

# Ensure uploads directory exists
os.makedirs("uploads", exist_ok=True)

# Static Stack Code Response (optional customization)
STACK_CODE_C = "..."  # You can add the stack code string here if needed

def extract_text_from_image(image_path):
    return pytesseract.image_to_string(Image.open(image_path))

@app.route('/')
def home():
    return render_template("cortana.html")

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get("message", "").lower()

    if "stack code in c" in user_input or "stack in c" in user_input:
        return jsonify(response=STACK_CODE_C)

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Cortana, a helpful coding assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return jsonify(response=response.choices[0].message.content)
    except Exception as e:
        return jsonify(response=f"Error: {str(e)}")

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify(response="No image file found.")
    file = request.files['image']
    if file.filename == '':
        return jsonify(response="No selected file.")
    filepath = os.path.join("uploads", file.filename)
    file.save(filepath)
    text = extract_text_from_image(filepath)
    return jsonify(response=text)

if __name__ == '__main__':
    app.run(debug=True)