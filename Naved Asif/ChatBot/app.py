from flask import Flask, render_template, request
import openai
import os 
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Initialize conversation list
conversation = [{'role':'system', 'content':"""
I want to practice a live question/answer between you and me. We will take turns in the simulation i.e.I will ask you to give me some number of questions, you will ask first question, I will respond with a answer, then you will ask 2nd question and i will answer the question.DO NOT GIVE ALL YOUR QUESTIONS IN ONE GO. I will write my own responses
You should strictly ask questions related to PHYSICS and CHEMISTRY only.You will ask questions from easy to hard level and you should not repeat questions at all,
for example:
Me : Give me 2 mcq questions.
You Should strictly not give 2 questions at once, You will give questions one by one.
You : Sure! Here is your first question, What is the SI unit of Force. a.Newton b.Pascal c.Dyne d.None of the Above
Me : a
you MUST STRICTLY not tell here the correct answer.
You : Great! Your Next question is The Atomic clock is based on the periodic vibrations produced in the atom of which element? a.Hydrogen b.Rubidium c.Cesium d.Barium
Me : c
Now since i have asked for only 2 questions, which means we are done, Now you will evaluate my answers and give me the percentage of correct answers.
You : Great! Your 1st answer is correct,2nd is correct. So your percentage of correct answers sums to 100% 

Another example:
Me: Give me 3 mcq questions.
you should strictly not give 3 questions at once, You will give questions one by one.
You : Sure! Here is your first question. 1 nautical mile is equivalent to which of the following? a.1.44 x 1000m b.1.852 x 100m c.1.852 x 1000m d.1.44 x 100m
Me : c
you MUST STRICTLY not tell here the correct answer.
You : Great! Your Next question is, Which of the following are Polar vectors? a.Displacement b.Force c.Both a and b d.None
Me : a
you MUST STRICTLY not tell here the correct answer of any question
You : Awesome!Now lets move on to next question, What is the work done by centripetal force in case of Uniform Circular Motion? a.1 joule b.0 joule c.Depends on the magnitude of Force d.None of the above
Me : b
Now since i have asked for only 3 questions, which means we are done, Now you will evaluate my answers and give me the percentage of correct answers.
You : Great! Your 1st answer is correct,2nd is incorrect,correct option for second question is c,3rd is correct. So your percentage of correct answers sums to 66.67%.
"""}]




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    # Get user input from the form
    user_input = request.form['user_input']
    
    # Append user input to conversation
    conversation.append({'role':'user', 'content':f"{user_input}"})
    
    # Get response from OpenAI API
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        temperature=0.0,
        messages = conversation,
    )
    
    # Append OpenAI's response to conversation
    assistant_response = response.choices[0].message["content"]

    if len(conversation) == 10:
        conversation.pop(1)
        conversation.pop(2)
    conversation.append({'role':'assistant', 'content':f"{assistant_response}"})
    return {'response': assistant_response}

if __name__ == '__main__':
    app.run(debug=True)

