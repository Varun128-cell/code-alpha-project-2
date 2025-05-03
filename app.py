from flask import Flask, request, jsonify, render_template
from translator import translate_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    source_text = data.get("text")
    source_lang = data.get("source_lang")
    target_lang = data.get("target_lang")
    translated = translate_text(source_text, source_lang, target_lang)
    return jsonify({"translated_text": translated})

if __name__ == '__main__':
    app.run(debug=True)
