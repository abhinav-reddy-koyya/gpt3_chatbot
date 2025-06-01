# 🧠 Cortana - AI Assistant Chatbot

**Cortana** is a modern AI-powered chatbot built with Flask and OpenAI's GPT-3.5 model. It features a sleek UI/UX, real-time animated conversations, and image-to-text extraction using OCR.

---

## ✨ Features

- 💬 Interactive chatbot powered by OpenAI GPT-3.5
- 🎨 Modern UI with animations, dark theme, and chat bubbles
- ⌨️ Keyboard "Enter" key support for sending messages
- 🖼️ Upload images and extract embedded text using OCR
- ✍️ Typing animation for bot replies
- ⚡ Smooth scroll & responsive layout

---

## 🛠 Tech Stack

| Layer        | Tech Used                  |
|--------------|----------------------------|
| Backend      | Python, Flask              |
| AI           | OpenAI GPT-3.5 (chat API)  |
| OCR (optional) | Tesseract via `pytesseract` |
| Frontend     | HTML, CSS, JavaScript      |

---

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/cortana-chatbot.git
cd cortana-chatbot

##CREATE A VIRTUAL ENVIRONMENT
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

#Install Dependencies
pip install -r requirements.txt

#Install Tesseract OCR
https://github.com/tesseract-ocr/tesseract
sudo apt update
sudo apt install tesseract-ocr

##Set your OpenAI API key
openai.api_key = "sk-XXXXXXXXXXXXXXXXXXXX"

##Running the App
python app.py
##Then open your browser at:
http://127.0.0.1:5000