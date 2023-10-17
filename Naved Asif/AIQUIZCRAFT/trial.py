from flask import Flask, render_template, request
import openai
from langchain.document_loaders import PyPDFLoader
import os 
from dotenv import load_dotenv
load_dotenv()
from langchain.document_loaders import PyPDFLoader
import PyPDF2
import re
import time
import json
import os
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Initialize conversation list to keep track of user inputs and AI responses
conversation = [{'role':'system', 'content':""" """}]

# Initialize a list to store text chunks extracted from PDF
texts = []

# Home page to upload the PDF file and start the conversation
@app.route('/', methods=['GET', 'POST'])
def index():
    global texts
    if request.method == 'POST':
        # Check if a file was uploaded
        global chunks
        if 'pdf' not in request.files:
            return redirect(request.url)

        # Save the uploaded PDF file
        pdf_file = request.files['pdf']
        pdf_path = "uploads/uploaded.pdf"
        pdf_file.save(pdf_path)

        # Extract text from the PDF and concatenate it into text_content
        text_content = ""
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            for i in range(1, num_pages):
                page = pdf_reader.pages[i]
                text_content += page.extract_text()

        # Split the text_content into smaller chunks using TokenTextSplitter
        from langchain.text_splitter import TokenTextSplitter
        text_splitter = TokenTextSplitter(chunk_size=3900, chunk_overlap=0)
        texts = text_splitter.split_text(text_content)
        print(len(texts))
    
    return render_template('index.html')

# Function to find numbers in a string using regular expressions
def find_number(string):
    pattern = r'\d+'  # Matches one or more digits
    matches = re.findall(pattern, string)
    return matches

# API endpoint to get AI-generated questions based on user input
@app.route('/get_response', methods=['POST'])
def get_response():
    # Get user input from the form
    global texts
    question_set = []
    user_input = request.form['user_input']
    num = find_number(user_input) # Extracting the number from user input using regex
    num_of_question = int(num[0]) # Typecasting the extracted number to an integer
    total_question_per_page = int(num_of_question / len(texts)) # Defining the number of questions to get from each chunk

    # If the remainder is not zero, add 1 to total questions per page
    if num_of_question % len(texts) != 0:
        total_question_per_page += 1

    # If total question is less than total chunks, set it to 1
    if total_question_per_page == 0:
        total_question_per_page = 1

    # Check if the total number of questions requested is greater than the available text chunks
    if num_of_question > len(texts) * 20:
        return {'response': f'Document Not Sufficient to frame {num_of_question} questions, Kindly give a number below {len(texts)*20}'}

    # Modify user input to get the desired output
    user_input = f"give me {total_question_per_page} questions"

    # Loop through each text chunk to get AI-generated questions
    for i in texts:
        # Modify the system message in the conversation list to include the current text chunk as CONTEXT
        conversation[0]['content'] = f"""You are a Question generator,You must give OUTPUT in JSON FORMAT

STEP 1: Strictly generate {total_question_per_page} questions from the below given CONTEXT

CONTEXT={i}

STEP 2: DO NOT REVEAL CONTEXT
 
STEP 3: You Must give OPTIONS in the below given FORMAT

FORMAT =[OPTION], [OPTION], [OPTION], [OPTION], ANSWER

STEP 4: Options of the questions must be RANDOMIZED, answer of every question should NOT BE SAME for all

STEP 5: You MUST GIVE OUTPUT IN JSON FORMAT.
"""

        # Append user input to conversation
        conversation.append({'role': 'user', 'content': f"{user_input}"})

        # Get response from OpenAI API
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            temperature=0.0,
            messages=conversation,
        )
        
        # Append OpenAI's response  to the question list
        assistant_response = response.choices[0].message["content"]
        json_response = json.loads(assistant_response)
        print(json_response)
        question_set.append(json_response["questions"])
        print("-------------------------------------------------------")
        
    
    
    formatted_questions = []

    for question_set in question_set:
        formatted_question_set = []
    
        for index, question_data in enumerate(question_set):
            question = {
                "createItem": {
                    "item": {
                        "title": question_data["question"],
                        "questionItem": {
                            "question": {
                                "required": True,
                                "grading": {
                                 "pointValue": 1,
                                    "correctAnswers": {
                                        "answers": [{"value": question_data["answer"]}]
                                 },
                                    "whenRight": {"text": "You got it!"},
                                    "whenWrong": {"text": "Sorry, that's wrong"}
                                },
                                "choiceQuestion": {
                                    "type": "RADIO",
                                    "options": [{"value": option} for option in question_data["options"]]
                                }
                            }
                        }
                    },
                    "location": {
                        "index": index
                    }
                }
            }
            formatted_question_set.append(question)

        formatted_questions.extend(formatted_question_set)

    # print(formatted_questions)

    NEW_QUESTION={"requests":formatted_questions}

# Set the OAuth 2.0 credentials.
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
    os.path.join(os.path.dirname(__file__), 'credentials.json'),
    'https://www.googleapis.com/auth/forms.body')

# Create the Google Forms API service object.
    service = build('forms', 'v1', credentials=credentials)

    form = {
        "info": {
            "title": "BC PORTFOLIO QUIZ-1",
        }
    }
    result = service.forms().create(body=form).execute()

    update = {
    "requests": [
        {
            "updateSettings": {
                "settings": {
                    "quizSettings": {
                        "isQuiz": True
                     }
                    },
                "updateMask": "quizSettings.isQuiz"
                }
            }
        ]
    }

# Converts the form into a quiz
    question_setting = service.forms().batchUpdate(formId=result["formId"],
                                                    body=update).execute()

    question_setting = service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION).execute()

    FormID=result["formId"]
# Prints the result to show the question has been added
    get_result = service.forms().get(formId=result["formId"]).execute()

    return {'response': f"Here is your link of GDOC: {get_result['responderUri']} and this is your form-id:- {FormID}"}



if __name__ == '__main__':
    app.run(debug=True, port=8080)
