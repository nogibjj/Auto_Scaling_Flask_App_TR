from dotenv import load_dotenv
import os
import requests
import json
import base64
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for,
    jsonify,
)
import openai


load_dotenv()
app = Flask(__name__)
openai.api_key = os.getenv("API_TOKEN")

@app.route("/")
def index():
    """retruns index page"""
    return render_template("index.html")

def get_completion(prompt, model="gpt-3.5-turbo"):
    prompt_answer = f"""
    Perform the following actions: 
    1 - Look up the list of requirements
    2 - Provide an alcohol drink based on the requirements from text
    3 - Return answer in seprate lines

    Using the following format:
    Drink name: <drink name>
    Estimated Time: <Estimated time cost of this dish>
    Recipe and Instructions: <>

    ```{prompt}```
    """
    
    print(prompt_answer)
    
    messages = [{"role": "user", "content": prompt_answer}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


@app.route('/result')
def result():
    # Get the result from the URL parameter
    result = request.args.get('result', '')
    print(result)
    return render_template('result.html', result=result)


@app.route("/predict", methods=["POST"])
def predict():
    """test predict"""
    print(request.form)
    prompt = request.form.get("prompt")
    print(prompt)
    result = get_completion(prompt)
    
    # return jsonify(result)
    return redirect(url_for('result', result=result))

if __name__ == "__main__":
    app.run(debug=True)
#     print(get_completion(prompt_answer))

