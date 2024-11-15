from flask import Flask, request, jsonify
import pickle
from keras.models import load_model # type: ignore
import numpy as np
from nltk.stem import WordNetLemmatizer
import json

# Inicializar Flask
app = Flask(__name__)

# Cargar modelo y datos
model = load_model('chatbot_model.h5')
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
lemmatizer = WordNetLemmatizer()

# Procesar entrada del usuario
def clean_up_sentence(sentence):
    sentence_words = sentence.split()
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

@app.route('/chat', methods=['POST'])
def chatbot_response():
    data = request.get_json()
    user_message = data['message']
    bow = bag_of_words(user_message, words)
    result = model.predict(np.array([bow]))[0]
    error_threshold = 0.25
    results = [[i, r] for i, r in enumerate(result) if r > error_threshold]
    results.sort(key=lambda x: x[1], reverse=True)
    if results:
        response = classes[results[0][0]]
    else:
        response = "No entiendo tu mensaje. ¿Podrías reformularlo?"
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
