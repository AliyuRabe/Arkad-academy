from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Define some responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "Doing well!", "Great, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["I'm not sure how to respond to that.", "Could you rephrase that?", "Interesting!"]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)