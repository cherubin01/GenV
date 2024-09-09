from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the generative AI model
genai.configure(api_key=os.getenv("AIzaSyDuAAibwe0zMecmlxjwnh-pwOeEK2RTvz8"))  # Ensure you have GENERATIVE_AI_API_KEY set in your environment variables

# Function to get response from Gemini model
def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text

# Initialize Flask app
app = Flask(__name__)

# Route for serving index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling POST request from frontend
@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        data = request.get_json()
        question = data['question']
        
        # Getting the response
        response = get_gemini_response(question)
        
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
