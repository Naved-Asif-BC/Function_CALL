import os
import json

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

# Set the OAuth 2.0 credentials.
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    os.path.join(os.path.dirname(__file__), 'credentials.json'),
    'https://www.googleapis.com/auth/forms.body')

# Create the Google Forms API service object.
service = build('forms', 'v1', credentials=credentials)


# Prints the responses of your specified form:
form_id = '<YOUR_FORM_ID>'

result = service.forms().responses().list(formId=form_id).execute()
print(result)